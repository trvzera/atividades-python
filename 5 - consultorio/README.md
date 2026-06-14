> **EN:** Flask exercise building a medical appointment panel where users search by specialty and view available doctors, CRM numbers, and accepted health plans.

---

# Painel de Consultas Médicas

Atividade em Python com **Flask** para praticar **rotas HTTP, formulários, templates Jinja2 e organização de módulos**: um painel web para buscar médicos por especialidade, com interface estilizada e dados fictícios.

## Status

**Concluído** — busca por especialidade funcional com validação de entrada e exibição de médicos, CRM e planos aceitos.

## Em que consiste

- **`app.py`** — aplicação Flask com rota principal (`GET`/`POST`) que renderiza o painel ou delega a busca ao módulo de consultório.
- **`consultorio.py`** — lógica de negócio com dicionário de especialidades e função `verificar_medicos()` para validar a busca e retornar os resultados.
- **`templates/painel.html`** — template Jinja2 com formulário de busca, mensagens de erro e grid de médicos encontrados.
- **`static/`** — estilos (`css/style.css`) e scripts (`js/main.js`) para feedback visual no envio do formulário e chips de sugestão.

## Especialidades disponíveis

| Especialidade   | Médicos |
|-----------------|---------|
| Cardiologia     | 2       |
| Pediatria       | 2       |
| Dermatologia    | 1       |

A busca ignora maiúsculas/minúsculas. Campos vazios e especialidades inexistentes exibem mensagens de erro amigáveis.

## Como executar

Certifique-se de ter Python 3 instalado.

1. Instale o Flask:
```bash
pip install flask
```

2. Execute a aplicação na raiz do projeto:
```bash
python app.py
```

3. Acesse no navegador:
```
http://127.0.0.1:5000
```

## Estrutura do projeto

```
atividade-consultorio/
├── app.py
├── consultorio.py
├── templates/
│   └── painel.html
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
└── README.md
```
