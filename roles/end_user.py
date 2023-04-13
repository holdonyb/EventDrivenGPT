from .chatbot_role import ChatBotRole
import json

class EndUser(ChatBotRole):
    def __init__(self):
        # Load role_definitions.json
        with open("roles/role_definitions.json", "r") as file:
            role_definitions = json.load(file)
        
        # Retrieve End User info and initialize the object
        end_user_info = role_definitions["End User"]
        super().__init__(
            role_name="End User",
            system_message=end_user_info["system_message"],
            tasks=end_user_info["tasks"],
            abilities=end_user_info["abilities"],
            response_format=end_user_info["response_format"]
        )

    def get_idea(self):
        # 与实际用户交互并获取项目想法
        user_idea = input("请描述您的项目想法：")
        return user_idea
