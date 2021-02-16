# coding=utf-8
from flask import Flask, session, redirect, url_for, render_template, request


def index():
    session["result"] = 0
    session["question_number"] = 1
    session["count"] = 0
    return redirect(url_for("gr_page"))


def gr_page():
    return render_template("gr_page.html")


def quiz_page():
    if len(questions) > session["count"]:
        return render_template("quiz_page.html", question_number=session["question_number"],
                               question=questions[session["count"]], answers=answer[session["count"]])
    else:
        return redirect(url_for("result"))


def update():
    if request.method == "POST":
        u_answer = request.form.get("name")
        if u_answer in right_answers:
            session["result"] += 20
    session["question_number"] += 1
    session["count"] += 1
    return redirect(url_for("quiz_page"))       


def result():
    return render_template("result.html", res=str(session["result"]))


questions = [
    "О каких минералах говорят «Воды боится, а из воды родится?»",
    "На какой естественный предмет больше всего похожа по своему строению Земля?",
    "Как называется веревка с петлей на конце?",
    """Древние греки называли ее «Борисфен», римляне «Данапарис», турки «Узу»
    Славяне «Славутич», как называется эта река сейчас?""",
    """Символом Рима является скульптурное изображение волчицы, Берлина- изображение медведя.
     А что является символом Копенгагена?"""
]

answer = [
    ("соль", "кальций", "мел", "кварц"),
    ("яблоко", "камень", "земля", "яйцо"),
    ("удавка", "верёвка", "лассо", "аркан"),
    ("дунай", "днепр", "дон", "дарковичи"),
    ("кот", "динозавр", "дракон", "русалочка")
]

right_answers = ["соль", "яйцо", "лассо", "днепр", "русалочка"]

app = Flask(__name__, static_folder="static", template_folder="templates")
app.config["SECRET_KEY"] = "secret@@key{}for[]quiz"
app.add_url_rule("/", "index", index, methods=["POST", "GET"])
app.add_url_rule("/gr_page", "gr_page", gr_page, methods=["POST", "GET"])
app.add_url_rule("/quiz_page", "quiz_page", quiz_page, methods=["POST", "GET"])
app.add_url_rule("/update", "update", update, methods=["POST", "GET"])
app.add_url_rule("/result", "result", result)

'''
if __name__ == "__main__":
    app.run()
'''