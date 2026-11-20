from flask import Flask, render_template

app= Flask(__name__)

# This is static page.
@app.route("/")
def home():
    first_name= "Mohit"
    last_name= "Negi"
    course= ["Python", "Flask", "Machine Learning", "SQL"]
    city= "Dehradun"
    price= 600
    return render_template("index.html", first_name= first_name,
    last_name= last_name,
    course= course,
    city= city,
    price= price)

if __name__== "__main__":
    app.run(debug= True)