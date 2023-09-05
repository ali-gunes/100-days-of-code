# In the class' next_question method, I created a recursion until it reaches question 12.
# When I create the object and call the next_question method for the first time, it will call the check_answer method if
# the user entered a valid input. In the check_answer method, at the end of the method, I am calling next_question again
# so it will repeat itself until the first if condition in the next_question method is false.
# When it's false (after all the questions has answered), it will prompt the user the quiz is finished
# and announce the score.

class QuizBrain:
    def __init__(self, question_bank):
        self.random_questions = question_bank
        self.question_number = 0
        self.score = 0
        self.user_answer = None

    def next_question(self):
        if self.question_number != len(self.random_questions):
            while True:
                print(
                    f"Category: {self.random_questions[self.question_number].category}\nDifficulty: {self.random_questions[self.question_number].difficulty.title()}")
                self.user_answer = input(
                    f"Q.{self.question_number + 1}: {self.random_questions[self.question_number].question_text} [True/False]:\t").lower()
                if self.user_answer not in ["true", "false"]:
                    print("Invalid input, please try again!")
                else:
                    self.check_answer()
                    break  # I am not sure if this is necessary?
        else:
            print("You've finished the quiz!")
            print(f"Your final score: {self.score}/{self.question_number}")
            print("Not bad... not bad at all!")

    def check_answer(self):
        if self.user_answer == self.random_questions[self.question_number].answer.lower():
            self.score += 1
            print(f"Your answer is correct! ✅")
        else:
            print(f"Your answer is incorrect! ❌")
        print(f"Score: {self.score}/{len(self.random_questions)}")
        print("\n")
        self.question_number += 1
        self.next_question()
