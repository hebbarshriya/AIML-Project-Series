# Simple Investment Assistent Chatbot

## Overview

This chatbot is designed to assist beginner and intermediate investors by providing information and basic know-how about investing. The chatbot covers topics such as benefits, bonds, risks, and mutual funds, offering insights and answering common queries.

## Features

- **User Management**: Register and log in users using SQLite database.
- **Interactive Quiz**: Encourages users to take a quiz for deeper insights.
- **Conversation Logging**: Logs chat history with timestamps for each user.

## Technologies Used

- **Python**: Core programming language for the chatbot.
- **SQLite**: Database for storing user information and chat logs.

## Setup Instructions

1. **Download the Directory**: 
    Ensure being in the same directory as the Pyhton script.
    

2. **Install Dependencies**:
    Ensure you have Python installed. Then, install the necessary packages:
    ```sh
    pip install sqlite3
    ```

3. **Initialize the Database**:
    Run the Python script to initialize the database:
    ```sh
    python chatbot.py
    ```

## How to Use

1. **Start the Chatbot**:
    Run the Python script to start the chatbot:
    ```sh
    python chatbot.py
    ```

2. **Interact with the Chatbot**:
    - **Get Information**: Users ask the chatbot questions about investments, benefits, risks etc.
    - **Take a Quiz**: To understand more about one's needs and various options of investing specific to them, take a quick quiz by responding to the prompts.
    - **End the Chat**: Type "end" to exit the chat.

## Example Prompts

- **General Info**: "I want to know about investing, can you tell me more about it ?"
- **Investment Benefits**: "What are some benefits of investments ?"
- **Investment Risks**: "I have heard there are some risks involving investments, can you give some insights ?"
- **About Bonds**: "How are bonds as an investing option ?"
- **About Mutual Funds**: "What are mutual funds ?"
- **To take the the quiz**: "What are my options as an ivestor ? or How do I begin my investment journey ? "
