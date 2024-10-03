import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from config.configuration import get_config
from util.generate_id import generate_id
from util.extract_table_of_content import *
from entity.textbook import Textbook
from model.database_connection import DatabaseConnection
from service.generator import Generator
from llm.agent import Agent
from openai import OpenAI



if  __name__ == "__main__":
    client = OpenAI(api_key=get_config()["api_key"])
    agent = Agent(client)
    db = DatabaseConnection()
    genai = Generator(agent=agent)

    course_name = "React"
    user_req = "This course should be prepared for the beginner."

    tb_title, tb_table, tb_preface = genai.generate_textbook(course_name=course_name, user_requirement=user_req)
    course_id = generate_id()
    textbook_id = generate_id()
    tb_table = extract_table_of_content(tb_table)
    tb_table_str = list_to_string(tb_table)

    new_textbook = Textbook(course_id=course_id,
                            textbook_id=textbook_id,
                            title=tb_title,
                            table=tb_table_str,
                            preface=tb_preface)
    
    db.add_textbook(new_textbook)

    print(new_textbook.stringify())