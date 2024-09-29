class Section:
    def __init__(self, course_id=None, textbook_id=None, chapter_id=None, section_id=None, number=None, title=None, concept=None, description=None, example=None):
        self.course_id = course_id
        self.textbook_id = textbook_id
        self.chapter_id = chapter_id
        self.section_id = section_id
        self.number = number
        self.title = title
        self.concept = concept
        self.description = description
        self.example = example

    def to_dict(self):
        return {
            'course_id': self.course_id,
            'textbook_id': self.textbook_id,
            'chapter_id': self.chapter_id,
            'section_id': self.section_id,
            'number': self.number,
            'title': self.title,
            'concept': self.concept,
            'description': self.description,
            'example': self.example
        }
