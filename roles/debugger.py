from .chatbot_role import ChatBotRole
from .executor import Executor
import json

class Debugger(ChatBotRole):
    def __init__(self):
        # Load role_definitions.json
        with open("roles/role_definitions.json", "r") as file:
            role_definitions = json.load(file)
        
        # Retrieve Debugger info and initialize the object
        end_user_info = role_definitions["Debugger"]
        super().__init__(
            role_name="Debugger",
            system_message=end_user_info["system_message"],
            tasks=end_user_info["tasks"],
            abilities=end_user_info["abilities"],
            response_format=end_user_info["response_format"]
        )
        self.executor = Executor()

    def fix_code(self, code, error):
        fixed_code = self.interact_with_chatbot(model="text-davinci-002", messages=[f"Fix this code based on the error: {error}. Code: {code}"])
        self.executor.update_code(code, error, fixed_code)
        return fixed_code
