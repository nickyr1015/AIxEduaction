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


    def get_title(self):
        return self.title
    
    def get_preface(self):
        return self.preface
    
    def ger_table(self):
        return self.table
    