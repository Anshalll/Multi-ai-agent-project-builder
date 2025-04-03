from google import genai
import os
from dotenv import load_dotenv
load_dotenv()



class Agents:
    def __init__(self):
        self.code = ""
        self.client = genai.Client(api_key=os.getenv("GiminiApikey"))

    
    def main_model(self, developer_agent_prompt , uprompt):
        response = self.client.models.generate_content(
            model="gemini-2.0-flash", contents=f"{developer_agent_prompt} \n {uprompt}"
        )
        return response.text
        


