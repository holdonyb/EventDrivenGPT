from .chatbot_role import ChatBotRole
import json
import shutil
import os
import openai

class Executor(ChatBotRole):
    def __init__(self):
        # Load role_definitions.json
        with open("roles/role_definitions.json", "r") as file:
            role_definitions = json.load(file)
        
        # Retrieve info and initialize the object
        executor_info = role_definitions["Executor"]
        super().__init__(
            role_name="Executor",
            system_message=executor_info["system_message"],
            tasks=executor_info["tasks"],
            abilities=executor_info["abilities"],
            response_format=executor_info["response_format"]
        )

    def parse_executor_content(self, content, expected_keys):
        openai.api_key = "your_openai_api_key"
        model = "text-davinci-002"

        # 提供更清晰的键定义
        key_definitions = {
            "filepath": "FILEPATH is the path to the file that needs to be created, edited, or saved.",
            "file_content": "FILE_CONTENT is the content that needs to be written to the file.",
            "target_class": "TARGET_CLASS is the name of the class where the new method should be appended.",
            "new_method": "NEW_METHOD is the code for the new method that should be appended to the target class.",
            "original_code": "ORIGINAL_CODE is the code that should be replaced with the new code.",
            "start_line_number": "START_LINE_NUMBER is the line number where the original code starts.",
            "new_code": "NEW_CODE is the code that should replace the original code in the file."
        }

        key_definitions_str = ', '.join([f'"{key}": {key_definitions[key]}' for key in expected_keys])

        openai_messages = [
            {"role": "system", "content": f"You are an AI language model that will parse the following executor content into a JSON object with keys {key_definitions_str}:"},
            {"role": "user", "content": f"The executor content is: {content}"}
        ]

        response = openai.ChatCompletion.create(model=model, messages=openai_messages)
        response_text = response.choices[0].text.strip()
        json_start = response_text.find("{")
        json_end = response_text.rfind("}") + 1
        json_text = response_text[json_start:json_end]

        try:
            content_parsed = json.loads(json_text)
            return content_parsed
        except json.JSONDecodeError:
            # 处理解析失败的情况
            return None

    def save_file(self, content):
        expected_keys = ["filepath", "file_content"]
        content_parsed = self.parse_executor_content(content, expected_keys)
        # 检查 content_parsed 是否为 None，处理解析失败的情况
        

        filepath = content_parsed["filepath"]
        file_content = content_parsed["file_content"]

        with open(filepath, "w") as file:
            file.write(file_content)

    def append_code(self, content):
        expected_keys = ["filepath", "target_class", "new_method"]
        content_parsed = self.parse_executor_content(content, expected_keys)
        # 检查 content_parsed 是否为 None，处理解析失败的情况

        filepath = content_parsed["filepath"]
        target_class = content_parsed["target_class"]
        new_method = content_parsed["new_method"]

        with open(filepath, "r") as file:
            lines = file.readlines()

        with open(filepath, "w") as file:
            for line in lines:
                file.write(line)
                if f"class {target_class}(" in line:
                    file.write("\n" + new_method)

    def update_code(self, filepath, original_code, start_line_number, content):
        # 从 content 中解析 new_code
        new_code = self.extract_new_code_from_content(content)
        if new_code is None:
            print("Failed to extract new_code from content.")
            return

        with open(filepath, "r") as file:
            lines = file.readlines()

        # 计算原始代码的结束行
        end_line_number = start_line_number
        while end_line_number < len(lines) and original_code not in lines[end_line_number]:
            end_line_number += 1

        # 如果原始代码未找到，处理异常情况
        if end_line_number == len(lines):
            print("Original code not found.")
            return

        # 替换代码
        lines[start_line_number:end_line_number + 1] = new_code.splitlines(True)

        # 写回文件
        with open(filepath, "w") as file:
            file.writelines(lines)

    def extract_new_code_from_content(self, content):
        # 定义期望的键
        expected_keys = ["new_code"]

        # 使用 parse_executor_content 函数解析 content
        parsed_content = self.parse_executor_content(content, expected_keys)

        # 如果解析成功，从 parsed_content 中获取 new_code
        if parsed_content is not None and "new_code" in parsed_content:
            return parsed_content["new_code"]
        else:
            return None
