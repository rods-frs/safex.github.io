from flask import Flask, render_template, request

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create_user')
def user_creation():
    return render_template('create_user.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    password = request.form.get('password')
    return f"Submitted Username: {username}, Password: {password}"

