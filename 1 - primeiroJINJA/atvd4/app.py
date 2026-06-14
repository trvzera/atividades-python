from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def page1():
    pessoas = ["ana", "pedro", "giovanni"]
    return render_template('page1.html', lista=pessoas)

if __name__ == '__main__':
    app.run(debug=True)