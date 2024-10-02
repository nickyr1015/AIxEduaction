import os
import sys
import pandas as pd
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from config.configuration import get_config
from entity.course import Course
from entity.chapter import Chapter
from entity.section import Section
from entity.textbook import Textbook
from util.generate_id import generate_id
from model.database_connection import DatabaseConnection



if __name__ == "__main__":
    db_conn = DatabaseConnection()

    """
    test course manipulation
    """

    # db_conn.remove_course_all()

    # new_course = Course(course_id=generate_id(), title="Data Structure", description="Introduction to Data Structure")
    # db_conn.add_course(new_course)
    # new_course = Course(course_id=generate_id(), title="Data Structure", description="Intermediate Data Structure")
    # db_conn.add_course(new_course)
    # new_course = Course(course_id=generate_id(), title="Data Structure", description="Complex Algorithms")
    # db_conn.add_course(new_course)
    # new_course = Course(course_id=generate_id(), title="Deep Learning", description="Computer Vision, Natural Language Processing")
    # db_conn.add_course(new_course)
    # new_course = Course(course_id=generate_id(), title="Machine Learning", description="Unsupervised Learning")
    # db_conn.add_course(new_course)

    # course = db_conn.get_course_all()
    # course = [c.to_dict() for c in course]

    # print("Get All Course Information")
    # for c in course:
    #     print(c)


    """
    test textbook manipulation
    """

    db_conn.remove_textbook_all()
    # new_textbook = Textbook(course_id=generate_id(),
    #                         textbook_id=generate_id(),
    #                         title="Deep Learning",
    #                         preface="This is a book talking about Deep Learning",
    #                         table="Table of Content for DL")
    # db_conn.add_textbook(new_textbook)

    # new_textbook = Textbook(course_id=1,
    #                         textbook_id=generate_id(),
    #                         title="Deep Learning",
    #                         preface="This is a book talking about Machine Learning",
    #                         table="Table of Content for ML")
    # db_conn.add_textbook(new_textbook)

    # new_textbook = Textbook(course_id=1,
    #                         textbook_id=123456,
    #                         title="Deep Learning",
    #                         preface="This is a book talking about Advance Machine Learning",
    #                         table="Table of Content for Advance ML")
    # db_conn.add_textbook(new_textbook)

    print("all textbooks")
    textbook_list = db_conn.get_textbook_all()
    for tb in textbook_list:
        print(tb.to_dict())

    # print("textbooks all of a course")
    # tb_list_under_course = db_conn.get_textbook_all_by_course_id(course_id=1)
    # for tb in tb_list_under_course:
    #     print(tb.to_dict())

    # textbook_id_list = db_conn.get_textbook_id_all_by_course_id(1)
    # for id in textbook_id_list:
    #     print(id)

    # updated_textbook = Textbook(course_id=1,
    #                         textbook_id=123456,
    #                         title="Deep Learning",
    #                         preface="This is a book talking about Profound Level Machine Learning",
    #                         table="Table of Content for Profound level ML")
    # db_conn.update_textbook_by_id(course_id=1, textbook_id=123456, new_textbook=updated_textbook)
    # print("textbook update")
    # tb_list_updated = db_conn.get_textbook_all()
    # for tb in tb_list_updated:
    #     print(tb.to_dict())


