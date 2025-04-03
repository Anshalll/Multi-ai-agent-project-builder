from src.Agents import Agents
import subprocess

tester_agent_prompt = """

    You are a code tester, your goal is to test the code and check if there is something wrong with the code.

    The error might involve indentation errors, syntax errors, or logic error.
    
    And one of the most comman issue is suppose we have :
        ```python
         import something 
         #entire code
         ```
         which is not correct. In this case i want you to make sure that the code always begins just belows the first quotes, example:
            ```python
            import something 
            #entire code
            ```
            now this is the correct format which i want so please make sure its in this format.
            
    Do not output anything accept code.
    Remove unnecessary in the code.
    """

class Tester(Agents):
    def checkCode(self , code):
        print("Testing the code")
      
        response = self.main_model(tester_agent_prompt, code )

        with open("coderunner.py" , "a") as f:
            f.write(response[10: -4])

        f.close()
        subprocess.run(["python" , "coderunner.py"])

tester = Tester()
