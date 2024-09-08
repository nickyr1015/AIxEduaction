from entity.textbook import Textbook

class Course:
    def __init__(self, textbook, description):
        """
        Properties (name: type):
        ---
        textbook: Textbook
        description: str
        
        """

        self.textbook = textbook
        self.description = description
