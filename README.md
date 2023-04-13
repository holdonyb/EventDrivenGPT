# Chatbot Roles Project

This project provides a framework for creating chatbots with different roles, such as Idea Generator, Programmer, Translator, and Executor. These chatbots interact with users and perform tasks related to their roles.

## Features

- A flexible chatbot framework with customizable roles.
- Predefined roles: Idea Generator, Programmer, Translator, and Executor.
- Each role has a specific set of tasks and abilities.
- Interaction with the chatbots through natural language processing, powered by OpenAI's GPT-4.

## Project Structure

- `main.py`: Entry point for the project, responsible for initializing and running the chatbots.
- `roles/`: Directory containing role definitions and implementation.
  - `role_definitions.json`: JSON file containing role information, such as system messages, tasks, abilities, and response formats.
  - `chatbot_role.py`: Base class for chatbot roles, providing core functionality for interacting with chatbots.
  - `idea_generator.py`: Implementation of the Idea Generator role.
  - `programmer.py`: Implementation of the Programmer role.
  - `translator.py`: Implementation of the Translator role.
  - `executor.py`: Implementation of the Executor role.

## How to Run

1. Install the required dependencies: `pip install -r requirements.txt`
2. Run the main script: `python main.py`
3. Interact with the chatbots through the command-line interface.

## Customization

To create a new chatbot role, follow these steps:

1. Add a new role definition in `role_definitions.json`, following the existing format.
2. Create a new Python file in the `roles/` directory, implementing the new role class.
3. Inherit from the `ChatBotRole` base class and implement the required methods for your role.
4. Update `main.py` to include your new role, if necessary.

Feel free to customize and extend the existing chatbot roles to suit your needs.
