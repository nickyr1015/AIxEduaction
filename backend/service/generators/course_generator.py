import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from prompt.course_prompt import *

class CourseGenerator:
    def __init__(self):
        pass

    def generate_course_title(self, agent, course_name):
        prompt = get_course_title(course_name)
        course_title = agent.call(prompt)
        return course_title
    
    def generate_course_description(self, agent, course_title):
        prompt = get_course_description(course_title)
        course_description = agent.call(prompt)
        return course_description
    