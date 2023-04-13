from .chatbot_role import ChatBotRole
import json
import subprocess

class Tester(ChatBotRole):
    def __init__(self):
        # Load role_definitions.json
        with open("roles/role_definitions.json", "r") as file:
            role_definitions = json.load(file)
        
        # Retrieve info and initialize the object

        tester_info = role_definitions["Tester"]
        super().__init__(
            role_name="Tester",
            system_message=tester_info["system_message"],
            tasks=tester_info["tasks"],
            abilities=tester_info["abilities"],
            response_format=tester_info["response_format"]
        )
        

    def run_test(self, test_file):
        # 运行测试文件并返回测试结果
        result = subprocess.run(["python", test_file], capture_output=True, text=True)
        if result.returncode == 0:
            return {"success": True, "error": None}
        else:
            return {"success": False, "error": result.stderr}