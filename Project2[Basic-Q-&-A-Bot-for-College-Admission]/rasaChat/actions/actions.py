# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

pgm_process = {"engineering" : "To apply for engineering, you need to visit our admissions portal and do the following:\n1. Fill out the application form\n2. Upload your 10th and 12th markcard\n3. Upload conduct and transfer certificate\n\n Desired field will be alloted based on performance in entrance test\n\n",
               "mba": "For MBA admissions, you should\n1. complete an online application\n2. provide your resume\n3. academic transcripts\n4. letters of recommendation\n5. statement of purpose.\n\n",
               "arts": "To pursue arts, you'll need to submit\n1. your portfolio\n2. academic transcripts\n3. letters of recommendation\n4. a personal statement showcasing your interest and achievements in the field.",
               "science": "For science programs, youll typically need to submit your\n1. academic transcripts\n2. letters of recommendation(atleast 1)\n3. admission test score\n4. a statement of purpose highlighting your research interests and goals."
        }   

requirements = {"engineering":"Eligibility criteria:\n1. Pass 10+2 or equivalent with Physics, Chemistry, and Mathematics as compulsory subjects.\n2. Secure at least 50% marks in aggregate.\n3. Appear for entrance test\n\n",
                "mba":"Eligibility criteria:\n1. Bachelor's degree in any discipline with a minimum aggregate of 50%\n2. 21 years of age\n3. Good rank in GMAT/CAT\n\n",
                "arts":"Eligibility criteria:\n1. Complete Class XII in any stream from a recognised board with a minimum aggregate percentage of 60%).\n2. Basic knowledge of Arts (Fine/ Visual/ Performing) subjects to which candidates are applying.\n\n",
                "science":"Eligibility criteria:\n1. 10+2 with minimum aggregate score of 45%\n2. Accepting Exams: JEE Main, JEE Advanced, KCET\n\n"}

information = {"engineering": "Great choice! Which field of engineering are you interested in? We have programs in Computer Science, Mechanical, Electrical, Civil and Chemical.",
        "mba": "Excellent! Which specialization are you looking for in MBA?  We have Marketing, Finance, HR, Operations, and International Business.",
        "arts": "Wonderful! Which subject do you want to pursue in Arts? We have English, History, Psychology and Philosophy",
        "science": "Good choice! Which field of science are you interested in? We have Physics, Chemistry, Biology, and Mathematics"}

course = {"engineering": ["computer science", "mechanical", "electrical", "civil" ,"chemical"],
          "mba":["marketing", "finance", "hr", "operations", "international business"],
          "arts":["english", "history", "psychology" ,"philosophy"],
          "science":["physics", "chemistry", "biology", "mathematics"]}

class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="I'm sorry, I didn't understand that. Can you please rephrase your question or ask something else about college admissions?")
        return []
    
class ActionProvideInfo(Action):
    def name(self) -> Text:
        return "action_provide_info"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        pgm = tracker.get_slot("pgm")
        try:
            info = information[pgm]
        except: info = "Bad_input"

        if info == "Bad_input":
            output="Im sorry. We do not offer this program"
        else:
            output = info

        dispatcher.utter_message(text=output)

        return []


class ActionProcessReq(Action):
    def name(self) -> Text:
        return "action_process_req"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        pgm = tracker.get_slot("pgm")
        try:
            process = pgm_process[pgm]
        except: process = "Bad_input"

        field = tracker.get_slot("field")
        try:
            req = requirements[pgm]
        except: req = "Bad_input"

        if field.lower() in course[pgm]:
            if process == "Bad_input":
                output="Im sorry. We do not offer this program"
            else:
                output = f"For {pgm} in {field}:\n{process}\n{req}"
        else:
            output = "Im sorry. This course is not offered by the institute"
        

        dispatcher.utter_message(text=output)

        return []


