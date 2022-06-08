from flask import Flask, request
from operations import add, sub, mult, div


app = Flask(__name__)

@app.get("/add")
def return_add():
    """Handle GET requests like /add?a=5&b=4"""

    a = int(request.args["a"])
    b = int(request.args["b"])

    return f"<h1>{a} + {b} = {add(a,b)}</h1>"

@app.get("/sub")
def return_sub():
    """Handle GET requests like /sub?a=5&b=4"""

    a = int(request.args["a"])
    b = int(request.args["b"])

    return f"<h1>{a} - {b} = {sub(a,b)}</h1>"

@app.get("/mult")
def return_mult():
    """Handle GET requests like /mult?a=5&b=4"""

    a = int(request.args["a"])
    b = int(request.args["b"])

    return f"<h1>{a} * {b} = {mult(a,b)}</h1>"

@app.get("/div")
def return_div():
    """Handle GET requests like /div?a=4&b=2"""

    a = int(request.args["a"])
    b = int(request.args["b"])

    return f"<h1>{a} / {b} = {div(a,b)}</h1>"