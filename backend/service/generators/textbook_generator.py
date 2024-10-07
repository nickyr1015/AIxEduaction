import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from prompt.textbook_prompt import *

class TextbookGenerator:
    def __init__(self):
        pass

    def generate_textbook_title(self, agent, course_name):
        prompt = get_textbook_title(course_name)
        textbook_title = agent.call(prompt)
        return textbook_title
    
    def generate_textbook_table(self, agent, course_name):
        prompt = get_textbook_table(course_name)
        table_of_content = agent.call(prompt)
        return table_of_content
    
    def generate_textbook_preface(self, agent, textbook_title, textbook_table):
        prompt = get_textbook_preface(textbook_title=textbook_title, textbook_table_of_content=textbook_table)
        table_of_content = agent.call(prompt)
        return table_of_content
    
    def generate_textbook(self, agent, course_name, user_requirement=None):
        context = "Your are a textbook."
        agent.add_context(context)
        if user_requirement != None:
            agent.add_context(user_requirement)
        
        textbook_title = self.generate_textbook_title(course_name=course_name)
        textbook_table = self.generate_textbook_table(course_name=course_name)
        textbook_preface = self.generate_textbook_preface(textbook_title=textbook_title, textbook_table=textbook_table)

        agent.clear_context()

        return textbook_title, textbook_table, textbook_preface
    