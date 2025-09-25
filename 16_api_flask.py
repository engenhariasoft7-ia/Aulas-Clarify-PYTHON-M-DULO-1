""""
 ____                               
| __ ) _   _  __ _ _ __   ___ __ _  
|  _ \| | | |/ _` | '_ \ / __/ _` | 
| |_) | |_| | (_| | | | | (_| (_| | 
|____/ \__, |\__,_|_| |_|\___\__,_| 
       |___/                         """











from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return " <h1> Bem vindo a minha pagina <h1> <a> Sobre <a> <br> saudacao </a>"

@app.route('/sobre')
def informacoes():
    return "<marquee> Maria Byanca </marquee>"

@app.route('/saudacao/<nome>')
def saudacao(nome):
    return f"<h1>Bem vindo </h1>{nome}!"

if __name__ == '__main__':
    app.run(debug=True)