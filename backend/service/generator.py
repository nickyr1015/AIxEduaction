from openai import OpenAI
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from config.configuration import get_config
from util.extract_table_of_content import extract_table_of_content
from prompt.textbook_prompt import get_textbook_table

class Generator:
    def __init__(self, agent):
        self.agent = agent

    def generate_table_of_content(self, textbook_name):
        prompt = get_textbook_table(textbook_name)
        response = self.agent.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
        {"role": "system", "content": "You are a text book"},
        {"role": "user", "content": prompt},
            ]
        )
        message = response.choices[0].message.content
        table_of_content = extract_table_of_content(message)
        return table_of_content
    


