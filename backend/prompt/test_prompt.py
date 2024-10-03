from openai import OpenAI
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from config.configuration import get_config
from util.extract_table_of_content import extract_table_of_content
from prompt.textbook_prompt import get_textbook_preface, get_textbook_table, get_textbook_title
from llm.agent import Agent




if __name__ == "__main__":
    client = OpenAI(api_key=get_config()["api_key"])
    agent = Agent(agent=client)
    context = "You are a textbook."
    agent.add_context(context)

    course_name = "React"
    title = agent.call(get_textbook_title(course_name))
    table = agent.call(get_textbook_table(course_name))
    preface = agent.call(get_textbook_preface(textbook_title=title, textbook_table_of_content=table))

    parsed_table = extract_table_of_content(table)

    print(f"{title}\n")
    print(f"{preface}\n")
    print(f"Table of Content:")
    for chapter in parsed_table:
        print(chapter)


