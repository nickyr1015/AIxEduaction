import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from config.configuration import get_config
from model.database_connection import DatabaseConnection
from util.writer import *

def sep():
    return "\n-------------------- seperation line --------------------\n"
def gap():
    return "\n\n"

if __name__ == "__main__":
    config = get_config()
    path_output = config["base_dir"]+"/backend/data/output/"
    filename = "react.txt"

    db = DatabaseConnection()
    course_id = 1072719

    course = db.get_course_by_id(course_id=course_id)
    # print(course.to_dict())
    text = ""
    text += course.title
    text += gap()
    text += course.description
    text += sep()

    textbook_id = 1906094
    textbook = db.get_textbook_by_id(course_id, textbook_id)
    text += textbook.title
    text += gap()
    text += textbook.preface
    text += gap()
    text += textbook.table
    text += sep()

    append_string_to_txt(path_output, filename, text)
    text = ""

    chapter_id_list = db.get_chapter_id_all_by_id(course_id, textbook_id)
    for chapter_id in chapter_id_list:
        chapter = db.get_chapter_by_id(course_id, textbook_id, chapter_id)
        text+=chapter.title
        text+=gap()
        text+=chapter.objective
        text+=sep()

        section_id_list = db.get_section_id_all_by_id(course_id, textbook_id, chapter_id)
        for section_id in section_id_list:
            section = db.get_section_by_id(course_id, textbook_id, chapter_id, section_id)
            text+=section.title
            text+=gap()
            text+=section.description
            text+=gap()
            text+=section.example
            text+=sep()

        text+=chapter.summary
        text+=sep()
        append_string_to_txt(path_output, filename, text)
        text = ""



