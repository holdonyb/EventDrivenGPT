from .product_manager import ProductManager
from .programmer import Programmer
from .tester import Tester
from .debugger import Debugger

from .chatbot_role import ChatBotRole
import json

class ProjectManager(ChatBotRole):
    def __init__(self):
        # Load role_definitions.json
        with open("roles/role_definitions.json", "r") as file:
            role_definitions = json.load(file)
        
        # Retrieve info and initialize the object
        project_manager_info = role_definitions["Project Manager"]
        super().__init__(
            role_name="Project Manager",
            system_message=project_manager_info["system_message"],
            tasks=project_manager_info["tasks"],
            abilities=project_manager_info["abilities"],
            response_format=project_manager_info["response_format"]
        )
        
    def init_roles(self, end_user, product_manager, programmer, debugger, tester, executor):
        self.end_user = end_user
        self.product_manager = product_manager
        self.programmer = programmer
        self.debugger = debugger
        self.tester = tester
        self.executor = executor

    def split_project(self, user_idea):
        # Use ChatGPT to analyze the user's idea and split the project into tasks
        tasks = self.interact_with_chatbot(model="gpt-3.5-turbo", messages=[f"Please split this project idea into tasks: {user_idea}"]).split('\n')
        return tasks

    def assign_next_role(self, task, current_role=None, feedback=None):
        if current_role is None:
            return self.product_manager
        elif isinstance(current_role, ProductManager) and feedback is not None:
            return self.programmer
        elif isinstance(current_role, Programmer) and feedback is not None:
            return self.tester
        elif isinstance(current_role, Tester) and feedback is not None:
            return self.debugger
        elif isinstance(current_role, Debugger) and feedback is None:
            return self.executor
        # Add more logic here based on the task, current_role, and feedback to assign the next role
