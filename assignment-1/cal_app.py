from flask import Flask, render_template, request

app = Flask(__name__)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    else:
        return x / y

history = []  # List to store calculation history

@app.route('/')
def index():
    return render_template('index.html', history=history)

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operation = request.form['operation']

    if operation == 'add':
        result = add(num1, num2)
        operation_str = 'Addition'
    elif operation == 'subtract':
        result = subtract(num1, num2)
        operation_str = 'Subtraction'
    elif operation == 'multiply':
        result = multiply(num1, num2)
        operation_str = 'Multiplication'
    elif operation == 'divide':
        result = divide(num1, num2)
        operation_str = 'Division'
    else:
        result = 'Invalid operation'
        operation_str = 'Invalid operation'

    # Append calculation to history
    history.append({'num1': num1, 'num2': num2, 'operation': operation_str, 'result': result})

    return render_template('index.html', result=result, num1=num1, num2=num2, history=history)

if __name__ == '__main__':
    app.run(debug=True)
