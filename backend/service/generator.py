from openai import OpenAI
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from prompt.textbook_prompt import *
from service.generators.textbook_generator import TextbookGenerator

class Generator:
    def __init__(self, agent):
        self.agent = agent
        self.textbook_generator = TextbookGenerator

    def generate_textbook_title(self, course_name):
        textbook_title = self.textbook_generator.generate_textbook(agent=self.agent, course_name=course_name)
        return textbook_title
    
    def generate_textbook_table(self, course_name):
        table_of_content = self.textbook_generator.generate_textbook(agent=self.agent, course_name=course_name)
        return table_of_content
    
    def generate_textbook_preface(self, textbook_title, textbook_table):
        table_of_content = self.textbook_generator.generate_textbook_table(agent=self.agent, textbook_title=textbook_title, textbook_table=textbook_table)
        return table_of_content
    
    def generate_textbook(self, course_name, user_requirement=None):
        textbook_title, textbook_table, textbook_preface = self.textbook_generator.generate_textbook(agent=self.agent, course_name=course_name)

        return textbook_title, textbook_table, textbook_preface
    
    def generate_course(self, course_name, user_requirement=None):
        pass

    


    


