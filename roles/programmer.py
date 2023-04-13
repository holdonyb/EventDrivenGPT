from .chatbot_role import ChatBotRole
from .executor import Executor
import json

class Programmer(ChatBotRole):
    def __init__(self):
        # Load role_definitions.json
        with open("roles/role_definitions.json", "r") as file:
            role_definitions = json.load(file)
        
        # Retrieve Programmer info and initialize the object
        programmer_info = role_definitions["Programmer"]
        super().__init__(
            role_name="Programmer",
            system_message=programmer_info["system_message"],
            tasks=programmer_info["tasks"],
            abilities=programmer_info["abilities"],
            response_format=programmer_info["response_format"]
        )
        self.executor = Executor()

    def develop_program(self, task, product_requirements):
        code = self.interact_with_chatbot(model="gpt-3.5-turbo", messages=[f"Develop a program for this task: {task}. Requirements: {product_requirements}"])
        return code

    def write_test(self, task):
        test_file = self.interact_with_chatbot(model="gpt-3.5-turbo", messages=[f"Write a test file for this task: {task}"])
        return test_file

