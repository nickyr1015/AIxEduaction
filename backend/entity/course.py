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

    def get_textbook(self):
        return self.textbook
    
    def get_description(self):
        return self.description
    
    def set_textbook(self, new_textbook):
        self.textbook = new_textbook

    def set_description(self, new_description):
        self.description = new_description