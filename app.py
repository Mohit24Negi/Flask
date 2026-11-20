from flask import Flask, render_template

app= Flask(__name__)

# This is static page.
@app.route("/")
def home():
    name= "Mohit"
    course= "Flask"
    city= "Dehradun"
    age= 28
    return render_template("index.html", name= name,
    course= course,
    city= city,
    age= age)

if __name__== "__main__":
    app.run(debug= True)