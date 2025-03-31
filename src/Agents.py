from google import genai
import os
from dotenv import load_dotenv
load_dotenv()



class Agents:
    def __init__(self):

        self.client = genai.Client(api_key=os.getenv("GiminiApikey"))
        


