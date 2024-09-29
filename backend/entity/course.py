from entity.textbook import Textbook

class Course:
    def __init__(self, course_id=None, title=None, description=None, textbook=None):
        self.course_id = course_id
        self.title = title
        self.description = description

    def to_dict(self):
        return {
            'course_id': self.course_id,
            'title': self.title,
            'description': self.description
        }