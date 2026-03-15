from flask import Flask, render_template, request
from models import Question, Result

app = Flask(__name__, template_folder="Assignment4.py/templates")

# Stack (LIFO) to store results
result_stack = []

questions = [
    Question("What does CPU stand for?",
    ["Central Processing Unit","Computer Personal Unit","Central Print Unit"],
    "Central Processing Unit"),

    Question("Which language is used with Flask?",
    ["Python","Java","C++"],
    "Python"),

    Question("HTML stands for?",
    ["Hyper Text Markup Language","High Text Machine Language","Hyper Tool Markup Language"],
    "Hyper Text Markup Language")
]

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/quiz')
def quiz():
    return render_template("quiz.html", questions=questions)

@app.route('/submit', methods=['POST'])
def submit():

    score = 0

    for i in range(len(questions)):
        user_answer = request.form.get(f"q{i}")
        if user_answer == questions[i].answer:
            score += 1

    result = Result(score)
    result_stack.append(result)

    return render_template("result.html", score=score, time=result.time)

if __name__ == '__main__':
    app.run(debug=True)