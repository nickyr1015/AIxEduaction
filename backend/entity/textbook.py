from entity.chapter import Chapter

class Textbook:
    def __init__(self, course_title, title, preface, table, chapter):
        self.course_title = course_title
        self.title = title
        self.preface = preface
        self.table = table
        self.chapter = chapter

    