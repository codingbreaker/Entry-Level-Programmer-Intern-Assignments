from flask import Flask, render_template, request

app = Flask(__name__)

# Render the index.html template when accessing the root URL
@app.route('/')
def index():
    return render_template('index.html')

# Handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    # Get form data
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Display the submitted data
    return render_template('submission.html', name=name, email=email, message=message)

if __name__ == '__main__':
    app.run(debug=True)
