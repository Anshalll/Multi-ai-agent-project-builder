from src.Agents import Agents
import os

developer_agent_prompt = """

        Your role is to generate code that a user desries in python. and you would have to wrap that code that a user wants into a function which writes the code into a file  , the name of the file is related to the kind of code a user wants and the file is inside the folder named generated.
        A user can also ask if there are any error in the code and you have to fix the code in the last code you just sent to the user!
        Print the output in plain text format!
        Do not print anything else unwanted including any comments or guide in the code!
        Output format:
        ```python
        <Generated Code>
        ```
    """

class Developer(Agents):

    def generate_code(self, uprompt):
        print("Agent is working!!")
        response = self.client.models.generate_content(
            model="gemini-2.0-flash", contents=f"{developer_agent_prompt} \n {uprompt}"
        )
        return response.text


    def savecode(self, output):
        
        code = output.strip()[10: -3]
        exec(code.strip())

    def runagent(self):
        while True:
            user_prompt = str(input("Enter what to do! "))
            if user_prompt == "q":
                break
            code = self.generate_code(user_prompt)
            self.savecode(code)

Developeragent = Developer()
