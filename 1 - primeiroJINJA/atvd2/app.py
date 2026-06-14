from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def page1():
    nome = "Giovanni"
    idade = 17
    return render_template('page1.html', nome=nome, idade=idade)

if __name__ == '__main__':
    app.run(debug=True)