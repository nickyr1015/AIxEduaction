from openai import OpenAI
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from service.generator import Generator
from model.database_connection import DatabaseConnection
from util.extract_table_of_content import *

class GenerationPipeline:
    def __init__(self, agent):
        self.agent = agent
        self.generator = Generator(self.agent)

    def sep(self):
        return "\n\n---------------------------------------------------------\n\n"
    
    def gap(self):
        return "\n\n\n"


    def save_string_to_txt(self, directory, filename, content):
        if not os.path.exists(directory):
            os.makedirs(directory)
        file_path = os.path.join(directory, filename)
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        
        print(f"File saved to {file_path}")

    def append_string_to_txt(self, directory, filename, content):
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        file_path = os.path.join(directory, filename)
        
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(content)
        
        print(f"Content appended to {file_path}")


    def generate_textbook_to_txt(self, course_name, user_requirement, directory, filename):
        self.agent.add_context("You are a Course")
        self.agent.add_context(user_requirement)

        course_title, course_description = self.generator.generate_course(course_name)
        self.append_string_to_txt(directory, filename, course_title+self.gap())
        self.append_string_to_txt(directory, filename, course_description+self.sep())

        self.agent.add_context(course_description)
        self.agent.add_context("You are a Textbook")

        textbook_title, textbook_table, textbook_preface = self.generator.generate_textbook(course_title)
        chapter_table = extract_table_of_content(textbook_table)
        chapter_table_string = list_to_string(chapter_table)

        self.append_string_to_txt(directory, filename, textbook_title+self.gap())
        self.append_string_to_txt(directory, filename, textbook_preface+self.gap())
        self.append_string_to_txt(directory, filename, chapter_table_string+self.sep())

        
        
        


