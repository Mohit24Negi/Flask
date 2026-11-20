from flask import Flask, request

app= Flask(__name__)

# multiple Query parameters
@app.route("/search")
def search():
    name= request.args.get("name", "Guest")
    last_name= request.args.get("last_name")
    course= request.args.get("course", "unknown")
    return f"{name} {last_name} is learning {course}"

if __name__== "__main__":
    app.run(debug= True)