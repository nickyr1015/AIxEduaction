import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from util.extract_table_of_content import *

class Textbook:
    def __init__(self, course_id=None, textbook_id=None, title=None, preface=None, table=None):
        self.course_id = course_id
        self.textbook_id = textbook_id
        self.title = title
        self.preface = preface
        self.table = table

    def to_dict(self):
        return {
            'course_id': self.course_id,
            'textbook_id': self.textbook_id,
            'title': self.title,
            'preface': self.preface,
            'table': self.table,
        }