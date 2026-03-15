from datetime import datetime

class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

class Result:
    def __init__(self, score):
        self.score = score
        self.time = datetime.now()

    def display(self):
        return f"Score: {self.score} | Time: {self.time}"