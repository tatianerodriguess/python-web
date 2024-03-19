from flask import Flask, render_template
 
app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('indice.html')
 
@app.route('/ola/')
@app.route('/ola/<nome>')
def ola(nome):
    return "Olá, " + nome

@app.route('/logar' , methods=['GET', 'POST'])
def logar():
    if request.method == 'POST':
        return "Recebeu post! Fazer login!"
    else:
        return "Recebeu get! Exibir Formulário de Login."
 
if __name__ == '__main__':
    app.run()