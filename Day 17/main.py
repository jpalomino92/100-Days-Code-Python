from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))

quizz = QuizBrain(question_bank)

while quizz.still_has_questions():
    quizz.next_question()

quizz.print_final()