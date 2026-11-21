from flask import Flask, render_template, request

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
        name= request.form.get("username")
        email= request.form.get("email")
        Message= request.form.get("Message")
        return f"Hello, {name}\n email:{email} \n Message: {Message}"
    return render_template("carrer.html")

@app.route("/search")
def search():
    query= request.args.get("query")
    return f"you searched for: {query}"

if __name__== "__main__":
    app.run(debug= True)