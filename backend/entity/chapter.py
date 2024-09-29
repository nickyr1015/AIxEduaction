class Chapter:
    def __init__(self, course_id=None, textbook_id=None, chapter_id=None, number=None, title=None, objective=None, summary=None):
        self.course_id = course_id
        self.textbook_id = textbook_id
        self.chapter_id = chapter_id
        self.number = number
        self.title = title
        self.objective = objective
        self.summary = summary

    def to_dict(self):
        return {
            'course_id': self.course_id,
            'textbook_id': self.textbook_id,
            'chapter_id': self.chapter_id,
            'number': self.number,
            'title': self.title,
            'objective': self.objective,
            'section': self.section,
            'summary': self.summary
        }