from openai import OpenAI
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from entity.course import Course
from entity.textbook import Textbook
from entity.chapter import Chapter
from entity.section import Section
from service.generator import Generator
from model.database_connection import DatabaseConnection
from util.extract_table_of_content import *
from util.generate_id import generate_id

class GenerationPipeline:
    def __init__(self, agent):
        self.agent = agent
        self.generator = Generator(self.agent)

    def generate_textbook(self, course_name, user_requirement):
        # Context Setup
        db = DatabaseConnection()
        self.agent.add_context("You are a Course")
        self.agent.add_context(user_requirement)

        # Generate Course and Save
        course_title, course_description = self.generator.generate_course(course_name)

        course_id_list = db.get_course_id_all()
        course_id = generate_id()
        while course_id in course_id_list:
            course_id = generate_id()

        new_course = Course(course_id=course_id, title=course_title, description=course_description)
        db.add_course(new_course)
        

        # Generate Textbook and Save
        self.agent.add_context(course_description)
        self.agent.add_context("You are a Textbook")

        textbook_title, textbook_table, textbook_preface = self.generator.generate_textbook(course_title)
        chapter_table = extract_table_of_content(textbook_table)
        chapter_table_string = list_to_string(chapter_table)

        textbook_id_list = db.get_textbook_id_all_by_id(course_id)
        textbook_id = generate_id()
        while textbook_id in textbook_id_list:
            textbook_id = generate_id()
        new_textbook = Textbook(course_id=course_id,
                                textbook_id=textbook_id,
                                title=textbook_title,
                                preface=textbook_preface,
                                table=chapter_table_string)
        db.add_textbook(new_textbook)


        # Generate Chapter
        chapter_id_list = db.get_chapter_id_all_by_id(course_id, textbook_id)

        for index in range(len(chapter_table)):
            chapter_title, chapter_objective, chapter_section, chapter_summary = self.generator.generate_chapter(chapter_table[index])
            
            chapter_id = generate_id()
            while chapter_id in chapter_id_list:
                chapter_id = generate_id()
            chapter_id_list.append(chapter_id)

            section_table = extract_table_of_content(chapter_section)
            new_chapter = Chapter(course_id=course_id,
                                  textbook_id=textbook_id,
                                  chapter_id=chapter_id,
                                  number=index,
                                  title=chapter_title,
                                  objective=chapter_objective,
                                  summary=chapter_summary
                                  )
            db.add_chapter(new_chapter)


            # Generate Section
            section_id_list = db.get_section_id_all_by_id(course_id, textbook_id, chapter_id)
            for idx in range(len(section_table)):
                section_title, section_description, section_example = self.generator.generate_section(section_table[idx])

                section_id_list = db.get_section_id_all_by_id(course_id, textbook_id, chapter_id)
                section_id = generate_id()
                while section_id in section_id_list:
                    section_id = generate_id()
                section_id_list.append(section_id)

                new_section = Section(course_id=course_id,
                                    textbook_id=textbook_id,
                                    chapter_id=chapter_id,
                                    section_id=section_id,
                                    number=idx,
                                    title=section_title,
                                    description=section_description,
                                    example=section_example
                                    )
                
                db.add_section(new_section)







        


        
        


