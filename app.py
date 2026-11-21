from flask import Flask, render_template, request, redirect, url_for

app= Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/carrer", methods= ["GET", "POST"])
def carrer():
    if request.method == "POST":
        name= request.form.get("name", "").strip()
        email= request.form.get("email", "").strip()
        age= request.form.get("age", "").strip()

        if not name:
            return "Name is Required"
        if not email:
            return "Name is Email"
        if not age:
            return "Name is Age"
        if not age.isdigit():
            return "Age Must be Number"
        age= int(age)
        return redirect(url_for("success"))
        
    return render_template("carrer.html")

@app.route("/reg-success")
def success():
    return "Registration successful"

if __name__== "__main__":
    app.run(debug= True)