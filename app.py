from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/comunidade')
def comunidade():
    return render_template('comunidade.html')

@app.route('/navegacao')
    return render_template('navegacao.html')

@app.route('/quemsomos')
    return render_template('quemsomos.html')

if __name__ == '__main__':
    app.run()

# Adicione outras rotas se necessário
