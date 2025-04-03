from src.Agents import Agents

developer_agent_prompt = """

        Your role is to generate code that a user desries.
 
        And you would have to wrap that code that a user wants into a function which writes the code into a file  , the name of the file is related to the kind of code a user wants and the file is inside the folder named generated.
        Make sure the indentation is correct!
        The generated code should be a raw string and you can use that raw string as a argument for a wrapped function.
        A user can also ask if there are any error in the code and you have to fix the code in the last code you just sent to the user!
        Print the output in plain text format!
        Do not print anything else unwanted including any comments or guide in the code!

        
    """

class Developer(Agents):
    def __init__(self):
        super().__init__()
        
    def generate_code(self, uprompt):
        print("Agent is working!!")
        response = self.main_model(developer_agent_prompt, uprompt )
       
        self.code = response[10: -4]



Developeragent = Developer()
