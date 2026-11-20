from flask import Flask, render_template

app= Flask(__name__)


@app.route("/")
def home():
    courses= ["Python", "Flask", "Machine Learning", "SQL"]
    student= {"Name" : "Mohit",
    "Course" : "Flask", 
    "City" : "Dehradun"}
    return render_template("index.html", courses= courses, student= student)

if __name__== "__main__":
    app.run(debug= True)