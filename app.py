from flask import Flask, render_template, request, abort, redirect, url_for, session
import os
import urllib.request
import json

app = Flask(__name__, 
        template_folder='techweek-frontend/templates', 
        static_folder='techweek-frontend/static')

app.secret_key = 'techweek2026secretkey'
DASHBOARD_USER = 'crisloginteste'
DASHBOARD_PASS = 'K9!vQ#72Lp@zR4mX'

SUPABASE_URL = os.environ.get('SUPABASE_URL')
SUPABASE_KEY = os.environ.get('SUPABASE_KEY')

def inserir_inscrito(dados):
    url = f"{SUPABASE_URL}/rest/v1/inscritos"
    body = json.dumps(dados).encode('utf-8')
    req = urllib.request.Request(url, data=body, method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('apikey', SUPABASE_KEY)
    req.add_header('Authorization', f'Bearer {SUPABASE_KEY}')
    urllib.request.urlopen(req)

def buscar_inscritos():
    req = urllib.request.Request(
        f"{SUPABASE_URL}/rest/v1/inscritos?select=*",
        headers={
            'apikey': SUPABASE_KEY,
            'Authorization': f'Bearer {SUPABASE_KEY}'
        }
    )
    return json.loads(urllib.request.urlopen(req).read())

@app.route("/")
def index(): 
    return render_template("index.html")

@app.route("/devs")
def devs(): 
    return render_template("devs.html")

@app.route("/palestrantes")
def palestrantes(): 
    return render_template("palestrantes.html")

@app.route("/perfil/<nome_url>")
def perfil(nome_url):
    # Removido abort(404) para permitir o carregamento da página de perfil
    return render_template("perfil.html", palestrante=nome_url)

@app.route("/ajuda")
def ajuda(): 
    return render_template("ajuda.html")

@app.route("/inscricao", methods=['GET', 'POST'])
def inscricao():
    if request.method == 'POST':
        dados = {
            'tipo':                 request.form.get('tipo'),
            'nome_completo':        request.form.get('nome'),
            'whatsapp':             request.form.get('whatsapp'),
            'ra':                   request.form.get('ra'),
            'cafe':                 request.form.get('cafe'),
            'curso_serie':          request.form.get('curso_serie'),
            'titulo_palestra':      request.form.get('titulo_palestra'),
            'bio':                  request.form.get('bio'),
            'email_palestrante':    request.form.get('email_palestrante'),
            'oq_sera_apresentado':  request.form.get('oq_sera_apresentado'),
            'tempo_palestra':       request.form.get('tempo_palestra'),
            'nome_projeto':         request.form.get('nome_projeto'),
            'desc_projeto':         request.form.get('desc_projeto'),
        }
        try:
            inserir_inscrito(dados)
            return render_template("sucesso.html")
        except Exception as e:
            return f"Erro ao gravar no banco: {e}"
    return render_template("inscricao.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
        if usuario == DASHBOARD_USER and senha == DASHBOARD_PASS:
            session['logado'] = True
            return redirect(url_for('dashboard'))
        return render_template("login.html", erro="Usuário ou senha incorretos")
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if not session.get('logado'):
        return redirect(url_for('login'))
    try:
        todos = buscar_inscritos()
        total = len(todos)
        alunos = len([x for x in todos if x.get('tipo') == 'aluno'])
        palestrantes = len([x for x in todos if x.get('tipo') == 'palestrante'])
        cafe = len([x for x in todos if x.get('cafe') == 'Sim'])
        projetos = len([x for x in todos if x.get('nome_projeto')])
        return render_template("dashboard.html",
            total=total,
            alunos=alunos,
            palestrantes=palestrantes,
            cafe=cafe,
            projetos=projetos,
            inscritos=todos
        )
    except Exception as e:
        return f"Erro: {e}"

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))