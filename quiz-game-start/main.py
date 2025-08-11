from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank : list[Question] = []

for question in question_data:
    question_bank.append(Question(question['text'],question['answer']))

q = QuizBrain(question_bank)

while q.has_questions():
    q.next_question()

print(f"You got total {q.points} points!")