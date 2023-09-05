# question_data = [
#     {"text": "A slug's blood is green.", "answer": "True"},
#     {"text": "The loudest animal is the African Elephant.", "answer": "False"},
#     {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
#     {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
#     {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, "
#              "you are free to take it home to eat.", "answer": "True"},
#     {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.",
#      "answer": "False"},
#     {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
#     {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
#     {"text": "Google was originally called 'Back-rub'.", "answer": "True"},
#     {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
#     {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
#     {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
# ]

# I used the OpenTDB's Trivia API to get a lot of trivia questions...
# This way I can get rid of the hard coded questions like above

# I am going to create an API request, read the JSON response and create the question bank
# To read JSON data, I am going to use urllib module and json module

from urllib.request import urlopen
import json
import html  # To decode the html entities in questions

# This url gives me 12 random trivia questions with mixed difficulties and categories
URL = "https://opentdb.com/api.php?amount=12&type=boolean"

api_response = urlopen(URL)

data_json = json.loads(api_response.read())  # json.loads() method reads and returns the JSON object

question_data = []

for data in data_json["results"]:
    category = data["category"]
    difficulty = data["difficulty"]
    text = html.unescape(data["question"])
    answer = data["correct_answer"]

    question_dict = {
        "category": category,
        "difficulty": difficulty,
        "text": text,
        "answer": answer,
    }

    question_data.append(question_dict)
