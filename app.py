from flask import Flask

app= Flask(__name__)

@app.route("/")
def home():
    return "welcome to home page"

@app.route("/user_name/<string:name>")
def user_name(name):
    return f"user name: {name}"

@app.route("/user_id/<int:id>")
def user_id(id):
    return f"user id: {id}"

@app.route("/price/<float:amount>")
def price(amount):
    return f"Price: {amount}"

# path converter
@app.route("/files/<path:file_path>")
def files(file_path):
    return file_path

# UUID converter
@app.route("/student/<uuid:user_id>")
def student(user_id):
    return str(user_id)

if __name__== "__main__":
    app.run(debug= True)