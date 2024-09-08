class Chapter:
    def __init__(self, number, title, objective, summary, section):
        self.number = number
        self.title = title
        self.objective = objective
        self.summary = summary
        self.section = section




class Section:
    def __init__(self, concept, example):
        self.concept = concept
        self.example = example