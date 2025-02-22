from flask import Flask, render_template
from flask import request
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/route32a")
def route32a():
    return render_template("index.html")

@app.route("/route")
def route():
    number=request.args.get('number')
    return "Hello from the {}".format(number)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8080')
