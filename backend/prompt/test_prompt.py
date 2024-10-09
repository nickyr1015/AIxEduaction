from openai import OpenAI
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from config.configuration import get_config
from util.extract_table_of_content import extract_table_of_content
from prompt.textbook_prompt import *
from prompt.course_prompt import *
from prompt.chapter_prompt import *
from prompt.section_prompt import *
from llm.agent import Agent

def sep(name = ""):
    print(f"\n---------------------------------------  {name}  ---------------------------------------\n")

if __name__ == "__main__":
    config = get_config()
    client = OpenAI(api_key=config["api_key"])
    agent = Agent(agent=client)

    course_name = "How to cook at home"

    context = "This is a course"
    user_requirement = "This is the cooking instructions for college students."

    # Course Prompt
    agent.add_context(context)
    agent.add_context(user_requirement)

    course_title_prompt = get_course_title(course_name)
    course_title = agent.call(course_title_prompt)

    course_description_prompt = get_course_description(course_title)
    course_description = agent.call(course_description_prompt)

    sep("course name")
    print(course_title)
    sep("course description")
    print(course_description)

    agent.clear_context()


    # Textbook Prompt
    context = "You are a textbook."
    agent.add_context(context)
    agent.add_context(user_requirement)

    textbook_title = agent.call(get_textbook_title(course_title))
    textbook_table = agent.call(get_textbook_table(course_title))
    textbook_preface = agent.call(get_textbook_preface(textbook_title=textbook_title, textbook_table_of_content=textbook_table))

    parsed_chapter_table = extract_table_of_content(textbook_table)

    sep("textbook title")
    print(textbook_title)
    sep("textbook preface")
    print(textbook_preface)
    sep("chapter table of content")
    for chapter in parsed_chapter_table:
        print(chapter)


    # Chapter Prompt
    chapter_one = parsed_chapter_table[3]
    chapter_objective_prompt = get_chapter_objective(chapter_one)
    chapter_objective = agent.call(chapter_objective_prompt)
    
    chapter_section_prompt = get_chapter_section(get_chapter_section(chapter_objective))
    chapter_section = agent.call(chapter_section_prompt)
    parsed_section_table = extract_table_of_content(chapter_section)

    chapter_summary_prompt = get_chapter_summary(chapter_title=chapter_one,
                                                 chapter_section=chapter_section,
                                                 chapter_objective=chapter_objective)
    chapter_summary = agent.call(chapter_summary_prompt)

    sep("chapter")
    print(chapter_one)
    sep("chapter objective")
    print(chapter_objective)
    sep("chapter knowledge checklist")
    for section in parsed_section_table:
        print(section)

    sep("chapter review summary")
    print(chapter_summary)


    # Section Prompt
    section_one = parsed_section_table[3]

    section_description_prompt = get_section_description(section_one)
    section_description = agent.call(section_description_prompt)

    section_example_prompt = get_section_example(section_one, section_description)
    section_example = agent.call(section_example_prompt)

    sep("concept")
    print(section_one)
    sep("description")
    print(section_description)
    sep("example")
    print(section_example)


