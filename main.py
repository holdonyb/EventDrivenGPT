from roles import end_user, project_manager, product_manager, programmer, debugger, tester, executor
from config import DEBUG
def main():
    user_idea = end_user.get_idea()
    tasks = project_manager.split_project(user_idea)
    product_requirements = product_manager.translate_user_idea(user_idea)

    for task in tasks:
        current_role = None
        feedback = None

        while True:
            next_role, operations = project_manager.assign_next_role(task, current_role, feedback)
            if DEBUG:
                print(f"Current role: {current_role}")
                print(f"Next role: {next_role}")
                print(f"Current feedback: {feedback}")
            if next_role == product_manager:
                feedback = product_manager.verify_task_requirements(task)
            elif next_role == programmer:
                code, test_file = programmer.develop_program(task, product_requirements)
            elif next_role == tester:
                test_result = tester.run_test(test_file)
                feedback = test_result["error"]
            elif next_role == debugger:
                code = debugger.fix_code(code, feedback)
                feedback = None
            elif next_role == executor:
                translated_code = executor.save_file(code)
                # Save translated code to the appropriate file
                break
            else:
                raise ValueError("Invalid role assignment")
            current_role = next_role

if __name__ == "__main__":
    main()
