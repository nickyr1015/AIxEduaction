from openai import OpenAI
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)


class Agent:
    def __init__(self, agent):
        self.agent = agent
        self.context = []

    def call(self, query):
        messages = []

        for context in self.context:
            messages.append(context)

        messages.append({"role": "user", "content": query})

        response = self.agent.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )
        return response.choices[0].message.content


    def add_context(self, context):
        self.context.append({"role": "system", "content": context})

    def clear_context(self):
        self.context = []