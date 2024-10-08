from openai import OpenAI
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from service.generators.textbook_generator import TextbookGenerator
from service.generators.chapter_generator import ChapterGenerator
from service.generators.section_generator import SectionGenerator
from service.generators.course_generator import CourseGenerator

class Generator:
    def __init__(self, agent):
        self.agent = agent
        self.course_generator = CourseGenerator()
        self.textbook_generator = TextbookGenerator()
        self.chapter_generator = ChapterGenerator()
        self.section_generator = SectionGenerator()


    def generate_textbook(self, course_title):
        textbook_title = self.textbook_generator.generate_textbook_title(self.agent, course_title)
        textbook_table = self.textbook_generator.generate_textbook_table(self.agent, textbook_title)
        textbook_preface = self.textbook_generator.generate_textbook_preface(self.agent, textbook_title, textbook_table)
        return textbook_title, textbook_table, textbook_preface
    
    def generate_course(self, course_name):
        course_title = self.course_generator.generate_course_title(self.agent, course_name)
        course_description = self.course_generator.generate_course_description(self.agent, course_title)
        return course_title, course_description
    
    def generate_chapter(self, chapter_title):
        chapter_objective = self.generate_chapter_objective(chapter_title)
        chapter_section = self.generate_chapter_section(chapter_objective)
        chapter_summary = self.generate_chapter_summary(chapter_title=chapter_title, chapter_section=chapter_section, chapter_objective=chapter_objective)
        return chapter_title, chapter_objective, chapter_section, chapter_summary
    
    def generate_section(self, section_title):
        section_description = self.generate_section_description(section_title)
        section_example = self.generate_section_example(section_title=section_title, section_description=section_description)
        return section_title, section_description, section_example


    """
    Implementation
    """
    

    def generate_textbook_title(self, course_name):
        textbook_title = self.textbook_generator.generate_textbook_title(agent=self.agent, course_name=course_name)
        return textbook_title
    
    def generate_textbook_table(self, course_name):
        table_of_content = self.textbook_generator.generate_textbook_table(agent=self.agent, course_name=course_name)
        return table_of_content
    
    def generate_textbook_preface(self, textbook_title, textbook_table):
        table_of_content = self.textbook_generator.generate_textbook_preface(agent=self.agent, textbook_title=textbook_title, textbook_table=textbook_table)
        return table_of_content
    
    def generate_course_title(self, course_name):
        course_title = self.course_generator.generate_course_title(agent=self.agent, course_name=course_name)
        return course_title
    
    def generate_course_description(self, course_title):
        course_description = self.course_generator.generate_course_description(agent=self.agent, course_title=course_title)
        return course_description
    
    def generate_chapter_objective(self, chapter_title):
        chapter_objective = self.chapter_generator.generate_chapter_objective(self.agent, chapter_title)
        return chapter_objective
    
    def generate_chapter_section(self, chapter_objective):
        chapter_section = self.chapter_generator.generate_chapter_section(self.agent, chapter_objective)
        return chapter_section
    
    def generate_chapter_summary(self, chapter_title, chapter_section, chapter_objective):
        chapter_summary = self.chapter_generator.generate_chapter_summary(self.agent, chapter_title=chapter_title,
                                                                        chapter_section=chapter_section,
                                                                        chapter_objective=chapter_objective)
        return chapter_summary
    
    def generate_section_description(self, section_title):
        section_description = self.section_generator.generate_section_description(self.agent, section_title)
        return section_description
    
    def generate_section_example(self, section_title, section_description):
        section_example = self.section_generator.generate_section_example(self.agent, section_title, section_description)
        return section_example    


    


    


