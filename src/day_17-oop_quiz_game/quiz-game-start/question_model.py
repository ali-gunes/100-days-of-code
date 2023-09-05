class Question:
    def __init__(self, category, difficulty, question_text, answer):
        self.category = category
        self.difficulty = difficulty
        # Above 2 lines are added later with API version of this project
        self.question_text = question_text
        self.answer = answer

