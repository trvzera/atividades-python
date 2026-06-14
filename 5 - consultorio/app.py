from flask import Flask, render_template, request
from consultorio import verificar_medicos

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
  if request.method == "POST":
    return verificar_medicos()
  return render_template(
    "painel.html",
    especialidade="",
    medicos="",
    erro="",
  )

if __name__ == "__main__":
  app.run(debug=True)