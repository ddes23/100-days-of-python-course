import random

class QuizBrain:
    def __init__(self, list):
        self.question_number = 0
        self.question_list = list
        self.score = 0

    def next_question(self):
        x = random.randint(0, (len(self.question_list) - 1))
        current_question = self.question_list[x]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text}  (True/False:) ")
        self.check_answer(user_answer, current_question.answer)
        del self.question_list[x]

    def still_has_questions(self):
        return len(self.question_list) > 0
    
    def check_answer(self, u_answer, c_answer):
        if u_answer.lower() == c_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong! Sorry!")
        print (f"The correct answer was {c_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")
          
