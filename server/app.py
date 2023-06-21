#!/usr/bin/env python3

from flask import Flask, abort

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_route(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    output = ""
    for i in range(parameter):
        output += str(i) + "\n"
    print(output)
    return output

@app.route('/math/<num1>/<operation>/<num2>')
def math_route(num1, operation, num2):
    
    if operation == '+':
        result = int(num1) + int(num2)
    elif operation == '-':
        result = int(num1) - int(num2)
    elif operation == '*':
        result = int(num1) * int(num2)
    elif operation == 'div':  # Handle division operation
        result = int(num1) / int(num2)
    elif operation == '%':  # Handle modulo operation
        result = int(num1) % int(num2)
    
    
    else:
        abort(400)  # Bad request

    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
