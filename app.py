from flask import Flask, render_template, request, redirect, url_for, flash

app= Flask(__name__)

app.secret_key= "change-this-in-prod"
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
            flash("Name is Required !", "danger")
            return redirect(url_for("carrer"))
            
        if not email:
            flash("Email is Required !", "danger")
            return redirect(url_for("carrer"))
        if not age:
            flash("Age is Required !", "danger")
            return redirect(url_for("carrer"))
        if not age.isdigit():
            return "Age Must be Number"
        age= int(age)
        flash("Registration successful !", "success")
        
    return render_template("carrer.html")

@app.route("/reg-success")
def success():
    return "Registration successful"

if __name__== "__main__":
    app.run(debug= True)