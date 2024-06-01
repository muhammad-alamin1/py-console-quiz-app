from quiz import Quiz
from question import *

if __name__ == "__main__":
    quiz = Quiz()
    
    quiz.add_question(q1)
    quiz.add_question(q2)
    quiz.add_question(q3)
    
    quiz.run_quiz()
    