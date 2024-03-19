from flask import Flask
 
app = Flask(__name__)

@app.route('/')
def index():
    return "Página principal."
 
@app.route('/ola/')
@app.route('/ola/<nome>')
def ola(nome):
    return "Olá, " + nome
 
if __name__ == '__main__':
    app.run()