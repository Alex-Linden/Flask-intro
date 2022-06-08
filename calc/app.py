from flask import Flask, request
from operations import add


app = Flask(__name__)

@app.get("/add")
def return_add():
    """Handle GET requests like /add?a=5&b=4"""

    a = int(request.args["a"])
    b = int(request.args["b"])

    sum = add(a,b)
    return f"<h1>{a} + {b} = {sum}</h1>"