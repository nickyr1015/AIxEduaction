import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from prompt.chapter_prompt import *

class ChapterGenerator:
    def __init__(self):
        pass

    def generate_chapter_objective(self, agent, chapter_title):
        prompt = get_chapter_objective(chapter_title)
        chapter_objective = agent.call(prompt)
        return chapter_objective
    
    def generate_chapter_section(self, agent, chapter_objective):
        prompt = get_chapter_section(chapter_objective)
        chapter_section = agent.call(prompt)
        return chapter_section
    
    def generate_chapter_summary(self, agent, chapter_title, chapter_section, chapter_objective):
        prompt = get_chapter_summary(chapter_title=chapter_title,
                                    chapter_section=chapter_section,
                                    chapter_objective=chapter_objective)
        chapter_summary = agent.call(prompt)
        return chapter_summary