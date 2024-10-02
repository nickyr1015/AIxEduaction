from openai import OpenAI
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from config.configuration import get_config
from util.extract_table_of_content import extract_table_of_content
from prompt.textbook_prompt import *

class Generator:
    def __init__(self, agent):
        self.agent = agent

    def generate_textbook_title(self, course_name):
        prompt = get_textbook_title(course_name)
        textbook_title = self.agent.call(prompt)
        return textbook_title
    
    def generate_textbook_table(self, course_name):
        prompt = get_textbook_table(course_name)
        table_of_content = self.agent.call(prompt)
        return table_of_content
    
    def generate_textbook_preface(self, textbook_title, textbook_table):
        prompt = get_textbook_preface(textbook_title=textbook_title, textbook_table_of_content=textbook_table)
        table_of_content = self.agent.call(prompt)
        return table_of_content
    
    def generate_textbook(self, course_name, user_requirement=None):
        context = "Your are a textbook."
        self.agent.add_context(context)
        if user_requirement != None:
            self.agent.add_context(user_requirement)
        
        textbook_title = self.generate_textbook_title(course_name=course_name)
        textbook_table = self.generate_textbook_table(course_name=course_name)
        textbook_preface = self.generate_textbook_preface(textbook_title=textbook_title, textbook_table=textbook_table)

        self.agent.clear_context()

        return textbook_title, textbook_table, textbook_preface


    


