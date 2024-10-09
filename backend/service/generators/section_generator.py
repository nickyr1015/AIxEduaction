import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from prompt.section_prompt import *

class SectionGenerator:
    def __init__(self):
        pass

    def generate_section_description(self, agent, section_title):
        prompt = get_section_description(section_title)
        section_description = agent.call(prompt)
        return section_description
    
    def generate_section_example(self, agent, section_title, section_description):
        prompt = get_section_example(section_title, section_description)
        section_example = agent.call(prompt)
        return section_example