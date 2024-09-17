from entity.textbook import Textbook

class Course:
    def __init__(self, title = None, description = None, textbook = None):
        self.title = title
        self.description = description
        self.textbook = textbook
