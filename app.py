from flask import Flask, render_template, request, abort
import os
import urllib.request
import json

app = Flask(__name__, 
        template_folder='techweek-frontend/templates', 
        static_folder='techweek-frontend/static')

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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))