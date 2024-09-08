from entity.chapter import Chapter

class Textbook:
    def __init__(self, title, preface, table, chapter):
        """
        Properties (name: type):
        ---
        title: str
        preface: str
        table: str[]
        chapter: Chapter

        """

        self.title = title
        self.preface = preface
        self.table = table
        self.chapter = chapter

    