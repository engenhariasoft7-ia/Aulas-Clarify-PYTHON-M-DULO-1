from flask import Flask, redirect, url_for,request, render_template
from requests import get

app = Flask(__name__)

@app.route('/')
def pagina_inicial():
    return render_template("inicio.html")

@app.route('/entrar/')
def fazer_login():
    return render_template('login.html')

@app.route('/pagina403/')
def pagina403():
    return render_template('pagina403.html')

@app.route('/welcome/')
def welcome():
    return render_template('welcome.html')

@app.route('/validador/', methods=['POST', 'GET'])
def validador():
    # credenciais fixas (exemplo didático)
    acesso_u = "Byanca"
    acesso_s = "123"

    if request.method == 'POST':
        usuario = request.form.get('c_usuario', '')
        senha = request.form.get('c_senha', '')
    else:  # GET (query string)
        usuario = request.args.get('c_usuario', '')
        senha = request.args.get('c_senha', '')

    if usuario == acesso_u and senha == acesso_s:
        return redirect(url_for('welcome'))
    else:
        return redirect(url_for('pagina403'))

if __name__ == '__main__':
    # Para desenvolvimento; em produção use um servidor WSGI.
    app.run('0.0.0.0')