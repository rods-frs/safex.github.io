from flask import Flask, render_template, request

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/create_user', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # Do not display the password in production! This is just for demonstration.
        return f"Submitted Username: {username}, Password: {password}"
    return render_template('create_user.html')

