from .chatbot_role import ChatBotRole
import json

class ProductManager(ChatBotRole):
    def __init__(self):
        # Load role_definitions.json
        with open("roles/role_definitions.json", "r") as file:
            role_definitions = json.load(file)
        
        # Retrieve info and initialize the object
        product_manager_info = role_definitions["Product Manager"]
        super().__init__(
            role_name="Product Manager",
            system_message=product_manager_info["system_message"],
            tasks=product_manager_info["tasks"],
            abilities=product_manager_info["abilities"],
            response_format=product_manager_info["response_format"]
        )

    def translate_user_idea(self, user_idea):
        requirements = self.interact_with_chatbot(model="gpt-3.5-turbo", messages=[f"Translate this user idea into requirements: {user_idea}"])
        print(requirements)
        return '\n'.join([requirement for requirement in requirements.split('\n') if "Next request" not in requirement])
        # return {requirement.split(':',1)[0].strip(): requirement.split(':',1)[1].strip() for requirement in requirements if "Next request" not in requirement}

    def verify_task_requirements(self, task):
        feedback = self.interact_with_chatbot(model="gpt-3.5-turbo", messages=[f"Verify the clarity and reasonableness of these task requirements: {task}"])
        return feedback if feedback.strip() else None
