from model import Question

class Quiz:
    def __init__(self):
        self.__questions = []
        self.__score = 0
    
    def add_question(self, question):
        self.__questions.append(question)
    
    def display_question(self, question):
        print(question.prompt)
        for op in question.option:
            print(op)
    
    def run_quiz(self):
        for question in self.__questions:
            self.display_question(question)
            guess = input("Enter your answer: ").strip().lower()
            if question.is_correct(guess):
                print("Correct!\n")
                self.__score += 1
            else:
                print(f"Wrong! The correct answer is {question.answer}\n")
        self.display_score()
    
    def display_score(self):
        print(f"Your Score is {self.__score}")