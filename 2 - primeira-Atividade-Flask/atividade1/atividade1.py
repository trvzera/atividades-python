from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Flask Python</h1> <p>O decorator são funções que modificam ou estendem o comportamento de outras funções, métodos ou classes sem alterar seu código original. \n E servem para modificar ou estender o comportamento de funções, métodos ou classes sem alterar seu código original. \nVocê digita @(nome da variavel instanciada com Flask).route('e o caminho aqui entre aspas')</p> "

if __name__ == '__main__':
    app.run(debug=True)