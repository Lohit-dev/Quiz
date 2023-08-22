

class QuizBrain:
    def __init__(self,questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)


    def nextquestion(self):
        question = self.questions_list[self.question_number].question
        self.question_number += 1
        answer = input(f"Q. {self.question_number}: {question} (True/False):")
        if answer == self.questions_list[self.question_number-1].answer:
            self.score+=1
            print("You got it right")
        else:
            print("Wrong answer")
        print(f"The correct answer is {self.questions_list[self.question_number-1].answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
