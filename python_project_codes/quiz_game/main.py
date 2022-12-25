# TODO: 1 Download app named BlockSite https://play.google.com/store/apps/details?id=co.blocksite&hl=en&gl=US
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    question = Question(text=item['question'], answer=item['correct_answer'])
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score score was {quiz.score}/{quiz.question_number}")