from flask import Flask, render_template, request
import csv

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/create_user', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        number_of_users = 0
        with open('users.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)
            for _ in reader:
                number_of_users += 1
        number_of_users += 1  # New user number
        with open('/home/rodsfrs/safex.github.io/safex/safex/users.csv', 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([number_of_users, username, password])
        return f"Submitted Username: {username}, Password: {password}, User Number: {number_of_users}"
    return render_template('create_user.html')
