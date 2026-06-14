from flask import render_template, request

dados_especialidades = {
    "cardiologia": [
        {"nome": "Dr. André Souza", "crm": "CRM/MG 18432", "planos": ["Unimed", "Amil", "SulAmérica"]},
        {"nome": "Dra. Fernanda Melo", "crm": "CRM/MG 22105", "planos": ["Bradesco Saúde", "Unimed"]},
    ],
    "pediatria": [
        {"nome": "Dra. Carla Nunes", "crm": "CRM/MG 15780", "planos": ["Unimed", "Hapvida", "Amil"]},
        {"nome": "Dr. Lucas Ribeiro", "crm": "CRM/MG 31209", "planos": ["SulAmérica", "NotreDame"]},
    ],
    "dermatologia": [
        {"nome": "Dra. Juliana Costa", "crm"    : "CRM/MG 29801", "planos": ["Amil", "Bradesco Saúde"]},
    ],
    }

def verificar_medicos():
    especialidade = request.form["especialidade"].lower()
    if especialidade == "":
        return render_template("painel.html", erro="Por favor, digite uma especialidade")
    if especialidade == "outer wilds":
        return render_template("painel.html", erro="Esse jogo é o melhor de todos, mas não temos médicos para essa especialidade.")
    if especialidade not in dados_especialidades:
        return render_template("painel.html", erro="Especialidade não encontrada")
    
    return render_template("painel.html", especialidade=especialidade, medicos=dados_especialidades[especialidade])
   
