# Chatbot Roles Project \[Under development, NOT READY YET\]

* This project is written with GPT-4 and GPT-3.5-Turbo (almost totally by GPT-4 actually)

This project provides a framework for creating an event-driven system using OpenAI's ChatGPT as different roles, to develop a new project automatically. The roles include End User, Project Manager, Product Manager, Programmer, Debugger, Tester, and Executor.

## Features

- A flexible event-driven system with different ChatGPT roles.
- End User: Provides basic ideas and needs in natural language.
- Project Manager: Manages the whole project, splits the project into tasks, and assigns them to different roles.
- Product Manager: Breaks down the user's idea and need into actual requirements that programmers will understand.
- Programmer: Develops programs following the instructions from the project manager and product manager, and writes test files for its own code.
- Debugger: Receives the results from the Tester and edits the code to make it work.
- Tester: Connects with the terminal and interpreter, implements the programmer's instructions, and sends errors and traceback information to the debugger.
- Executor: Translates the programmer's output into operations, including creating, editing, and saving files.

## Project Structure

- `main.py`: Entry point for the project, responsible for initializing and running the event-driven system. It creates instances of the various roles, handles user input, and coordinates communication between the roles.
- `requirements.txt`: Lists required dependencies for the project, ensuring proper package installation for smooth operation.
- `config.py`: Configuration file for the project, including OpenAI API key and other settings. Allows for centralized management of project-wide configurations.
- `roles/`: Directory containing role definitions and implementation.
  - `__init__.py`: Initializes the `roles` package, making it easy to import and use the role classes in other parts of the project.
  - `role_definitions.json`: JSON file containing role information, such as system messages, tasks, abilities, and response formats. Provides a clear overview of each role's capabilities and responsibilities.
  - `end_user.py`: Defines the End User role, which accepts user input in the form of natural language and communicates the user's ideas and needs to the other roles.
  - `project_manager.py`: Implements the Project Manager role, which oversees the project, breaks it down into tasks, and assigns those tasks to appropriate roles. It also monitors progress and manages resources.
  - `product_manager.py`: Handles the Product Manager role, which takes the user's ideas and needs from the End User role and translates them into clear and concise requirements that can be understood by the Programmer role.
  - `programmer.py`: Provides the Programmer role, which develops code based on the instructions received from the Project Manager and Product Manager roles. This role is also responsible for writing test files for its own code.
  - `debugger.py`: Implements the Debugger role, which analyzes test results and error messages provided by the Tester role, and corrects any issues found in the code.
  - `tester.py`: Defines the Tester role, which connects with the terminal and interpreter to execute the code developed by the Programmer role. It then reports any errors and traceback information to the Debugger role for further analysis.
  - `executor.py`: Implements the Executor role, which translates the instructions from the Programmer role into operations, such as creating, editing, and saving files. It carries out these operations in response to the Programmer's output.
- `tests/`: Directory containing test files for different roles.
  - `__init__.py`: Initializes the `tests` package.
  - `test_programmer.py`: Test cases for the Programmer role.
  - `test_translator.py`: Test cases for the Translator role.

## How to Run

1. Install the required dependencies: `pip install -r requirements.txt`
2. Set up the OpenAI API key in `config.py`.
3. Run the main script: `python main.py`
4. Interact with the event-driven system through the command-line interface.

## Customization

To create a new ChatGPT role or modify an existing role, follow these steps:

1. Add or update the role definition in `role_definitions.json`, following the existing format.
2. Create a new Python file in the `roles/` directory, implementing the new role class, or modify an existing file.
3. Inherit from the `ChatBotRole` base class (if applicable) and implement the required methods for your role.
4. Update `main.py` to include your new role or modifications, if necessary.

Feel free to customize and extend the existing ChatGPT roles to suit your needs.
