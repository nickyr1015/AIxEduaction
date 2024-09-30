from openai import OpenAI
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from config.configuration import get_config
config = get_config()
client = OpenAI(api_key=config['api_key'])


class Agent:
    def __init__(self, agent):
        self.agent = agent
        self.context = None

    def call(self, query):
        messages = []

        if self.context != None:
            messages.append({"role": "system", "content": self.context})

        messages.append({"role": "user", "content": query})

        response = self.agent.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )
        return response.choices[0].message.content


    def add_context(self, context):
        self.context = context