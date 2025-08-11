from question_model import Question

class QuizBrain:
    def __init__(self, q_list) -> None:
        self.question_number = 0
        self.question_list = q_list
        self.points = 0
    
    def next_question(self):
        self.current_question: Question = self.question_list[self.question_number]
        user_ans = input(f"Q.{self.question_number}) Question: {self.current_question.text} (True/False).\n")
        self.question_number += 1
        if self.check_answer(user_ans,self.current_question):
            self.points+=1
        if self.has_questions():
            print(f"Current points: {self.points}")

    def has_questions(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self,user_answer : str , question : Question) -> bool:
        return user_answer.strip().lower() == question.answer.strip().lower()