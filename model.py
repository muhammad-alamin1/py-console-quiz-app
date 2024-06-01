class Question:
    def __init__(self, prompt, option, answer):
        self.prompt = prompt
        self.option = option
        self.answer = answer
    
    def is_correct(self, guess):
        return guess == self.answer
    