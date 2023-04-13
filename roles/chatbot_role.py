import openai
from config import API_KEY, MODEL, DEBUG
from typing import List
import json
import re
openai.api_key = API_KEY

class ChatBotRole:
    def __init__(self, role_name: str, system_message: str, tasks: List[str], abilities: List[str], response_format: str):
        self.role_name = role_name
        self.system_message = system_message
        self.tasks = tasks
        self.abilities = abilities
        self.response_format = response_format

    def interact_with_chatbot(self, model, messages, return_json=False):
        # Combine system_message, tasks, abilities, and response_format
        combined_system_message = (
            f"{self.system_message}\n"
            f"Tasks: {', '.join(self.tasks)}\n"
            f"Abilities: {', '.join(self.abilities)}\n"
            f"Response Format: {self.response_format}"
        )

        openai_messages = [
            {"role": "system", "content": combined_system_message}
        ]

        for message in messages:
            openai_messages.append({"role": "user", "content": f"{self.role_name}: {message}"})

        chat_history = []
        if DEBUG:
            print("Role: ", self.role_name, "Model: ", model, sep="\n")
        for i in range(5):  # 每次最多对话3轮
            if DEBUG:
                print(f"===== {i} =====")
                print(openai_messages)
            response = openai.ChatCompletion.create(model=model, messages=openai_messages)
            chat_history.extend(response['choices'])
            if chat_history[-1]['finish_reason'] in ['stop', 'null', 'content_filter']:
                break

            openai_messages = []
            for choice in chat_history:
                openai_messages.append({"role": choice['role'], "content": choice['message']['content']})

        messages = []
        for choice in chat_history:
            messages.append(choice['message']['content'])
        
        message =  "\n".join(messages)
        if DEBUG:
            print("===== Final =====")
            print(message)
        if return_json:
            # 如果希望返回json格式，那么从message中读取json
            json_str = re.findall(r'{.*}', message, flags=re.DOTALL)
            if json_str:
                message = json.loads(json_str[0])
            else:
                message = None
        return message