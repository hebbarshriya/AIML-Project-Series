# College Admission Chatbot

This is a College Admission Chatbot built using the Rasa framework. The bot assists prospective students by answering queries related to college admissions, courses, application processes, deadlines, and more.

## Table of Contents

- [Features](#features)
- [Example Queries](#example-queries)
- [Installation](#installation)
- [Configuration Files](#configuration-files)
  - [nlu.yml](#nluyml)
  - [domain.yml](#domainyml)
  - [stories.yml](#storiesyml)
  - [rules.yml](#rulesyml)
  - [actions.py](#actionspy)
  - [test_stories.yml](#test_storiesyml)
- [Training the Bot](#training-the-bot)
- [Running the Bot](#running-the-bot)
- [Testing the Bot](#testing-the-bot)


## Features

- **Intuitive Conversations**: Capable of understanding and responding to a variety of queries related to college admissions.
- **Course and Program Information**: Provides information about the courses and programs offered by the college.
- **Deadline Information**: Offers information on important deadlines for applications.
- **Campus Facilities**: Shares details about the facilities available on campus.
- **Contact Information**: Provides contact details for the admissions office.
- **Scholarship Information**: Guides users on available scholarships and financial aid.
- **Custom Responses**: Ability to handle custom queries and provide relevant information.

## Example Queries

Here are some example queries the chatbot can answer:

- **General Greetings and Farewells**:
  - "Hello there!"
  - "Goodbye!"
  
- **Admission Procedures**:
  - "What is the procedure for admission?"
  - "How can I apply for admission?"
  
- **Deadlines**:
  - "What is the deadline for submitting my application?"
  - "When is the last date to apply?"
  
- **Facilities**:
  - "What facilities are available on campus?"
  - "Does the campus have a library?"
  
- **Contact Information**:
  - "How can I contact the admissions office?"
  - "What is the phone number of the college?"
  
- **Scholarships**:
  - "Are there any scholarships available?"
  - "How can I apply for financial aid?"

- **Courses and Programs**:
  - "What courses do you offer?"
  - "Tell me about the engineering program."
  - "Can you provide details on the computer science field?"
  - "What are the arts courses available?"


## Installation

1. **Download the Directory**:

2. **Install Rasa**:
   ```bash
   pip install rasa
   ```

## Configuration Files

### nlu.yml

This file contains training data for the Natural Language Understanding (NLU) component of the chatbot. It includes various intents that the bot can recognize, such as `greet`, `goodbye`, `affirm`, `deny`, `procedure`, `status_check`, `deadlines`, `facilities`, `contact`, `scholarship`, `choose_pgm`, `choose_field`, `random`, and `agreement`. Each intent has a set of example phrases that users might say to express that intent.

### domain.yml

This file defines the bot's intents, entities, slots, responses, and actions. It outlines the structure and elements the bot uses to interact with users.

### stories.yml

The `stories.yml` file contains training stories, which are example conversations that help the bot learn how to respond in different scenarios. These stories map out the dialogues between the user and the bot.

### rules.yml

The `rules.yml` file defines the rules for specific bot behaviors. These rules help the bot determine the appropriate actions to take based on user inputs.

### actions.py

The `actions.py` file contains custom action code. These actions are Python functions that the bot can execute in response to specific intents or slots being set.

### test_stories.yml

This file contains test stories to evaluate that your bot behaves as expected. It includes predefined conversation paths to test the bot's responses to various user inputs. These tests help ensure that the bot performs correctly in different scenarios.

## Training the Bot

Before running the bot, you need to train it using the Rasa CLI:

```bash
rasa train
```

This command processes the data in the `nlu.yml`, `domain.yml`, `stories.yml`, and `rules.yml` files to create a machine learning model for the chatbot.

## Running the Bot

To start the Rasa server and interact with the bot, run:

```bash
rasa shell
```

This command will launch the Rasa shell where you can chat with the bot directly in your terminal.

For a more interactive experience, you can run the action server and the Rasa server in separate terminals:

1. **Run the action server**:
   ```bash
   rasa run actions
   ```

2. **Run the Rasa server**:
   ```bash
   rasa run
   ```

## Testing the Bot

To ensure that the bot behaves as expected, you can run the test stories provided in `test_stories.yml`:

```bash
rasa test
```

This command will execute the test stories and provide a report on the bot's performance. The test stories cover various user intents and the expected bot responses, ensuring the bot's behavior is validated.
