from flask import Flask, render_template, request, render_template_string

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/usercreation')
def user_creation():
    return render_template_string('''
        <form action="/create_user" method="post">
            <input type="text" name="username" placeholder="Username" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">Create User</button>
        </form>
    ''')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    password = request.form.get('password')
    return f"Submitted Username: {username}, Password: {password}"

