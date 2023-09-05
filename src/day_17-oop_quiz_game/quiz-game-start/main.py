from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random

question_bank = []
for question in question_data:
    new_q = Question(question["category"], question["difficulty"], question["text"], question["answer"])
    question_bank.append(new_q)

random.shuffle(question_bank)  # Shuffled the list because I wanted to have random questions each time
# for question in question_bank:
#     print(f"{question.question_text}:\t{question.answer}")

print("""
  _______             ___    ______    _         ___  
 |__   __|           |__ \  |  ____|  | |       |__ \ 
    | |_ __ _   _  ___  ) | | |__ __ _| |___  ___  ) |
    | | '__| | | |/ _ \/ /  |  __/ _` | / __|/ _ \/ / 
    | | |  | |_| |  __/_|   | | | (_| | \__ \  __/_|  
    |_|_|   \__,_|\___(_)   |_|  \__,_|_|___/\___(_)
""")
play = input("Welcome to the Quiz Game! Do you want to play? [y/n]:\t").lower()

if play == "y":
    print("Excellent! You will be answering 12 questions with mixed difficulty levels and categories!\nGood luck!\n\n")
    quiz = QuizBrain(question_bank)
    quiz.next_question()
else:
    print("Goodbye")
