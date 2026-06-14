from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def page1():
    notas = {
        "ana": 2, 
        "pedro": 3,
        "arthur": 4, 
        "felipe": 5, 
        "giovanni": 6, 
        "henrique": 7
        }
    return render_template('page1.html', lista=notas)

if __name__ == '__main__':
    app.run(debug=True)