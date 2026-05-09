from flask import Flask, render_template, request, abort
import os
import urllib.request
import json

# --- CONFIGURAÇÃO DE CAMINHOS ---
base_dir = os.path.abspath(os.path.dirname(__file__))
path_projeto = os.path.join(base_dir, 'techweek-frontend')

if os.path.exists(path_projeto):
    template_dir = os.path.join(path_projeto, 'templates')
    static_dir = os.path.join(path_projeto, 'static')
else:
    template_dir = os.path.join(base_dir, 'templates')
    static_dir = os.path.join(base_dir, 'static')

app = Flask(__name__, 
            template_folder=template_dir, 
            static_folder=static_dir)

# --- BANCO DE DADOS (SUPABASE) ---
SUPABASE_URL = os.environ.get('SUPABASE_URL', '')
SUPABASE_KEY = os.environ.get('SUPABASE_KEY', '')

def inserir_inscrito(dados):
    # Se as variáveis de ambiente não estiverem configuradas, ignora silenciosamente
    if not SUPABASE_URL or not SUPABASE_KEY:
        print("[AVISO] SUPABASE_URL ou SUPABASE_KEY não configurados. Dados não gravados.")
        return

    url = f"{SUPABASE_URL}/rest/v1/inscritos"
    body = json.dumps(dados).encode('utf-8')
    req = urllib.request.Request(url, data=body, method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('apikey', SUPABASE_KEY)
    req.add_header('Authorization', f'Bearer {SUPABASE_KEY}')
    req.add_header('Prefer', 'return=minimal')  # Evita erro 406 do Supabase
    urllib.request.urlopen(req)

# --- DADOS DOS PALESTRANTES ---
PALESTRANTES_DADOS = {
    'bruno': {
        'nome': 'Bruno Silva',
        'trilha': 'IA & DADOS',
        'sub_titulo': 'Especialista em visão computacional',
        'descricao_completa': 'Bruno atua na vanguarda da Inteligência Artificial, com foco em processamento de linguagem natural e modelos preditivos de larga escala.',
        'imagem': 'bruno.jpg'
    },
    'heitor': {
        'nome': 'Heitor Santos',
        'trilha': 'DESENVOLVIMENTO',
        'sub_titulo': 'Arquiteto de Software',
        'descricao_completa': 'Heitor possui anos de experiência construindo sistemas robustos e escaláveis, focando sempre em performance e segurança da informação.',
        'imagem': 'heitor.jpeg'
    }
}

# --- ROTAS ---

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
    dados = PALESTRANTES_DADOS.get(nome_url.lower())
    if not dados:
        abort(404)
    return render_template("perfil.html", palestrante=dados)

@app.route("/ajuda")
def ajuda(): 
    return render_template("ajuda.html")

@app.route("/inscricao", methods=['GET', 'POST'])
def inscricao():
    if request.method == 'POST':
        dados = {
            'tipo':             request.form.get('tipo'),
            'nome_completo':    request.form.get('nome'),
            'whatsapp':         request.form.get('whatsapp'),
            'ra':               request.form.get('ra'),
            'cafe':             'sim' if request.form.get('cafe') else 'nao',
            'curso_serie':      request.form.get('curso_serie'),
            'titulo_palestra':  request.form.get('titulo_palestra'),
            'bio':              request.form.get('bio'),
            'nome_projeto':     request.form.get('nome_projeto'),
            'desc_projeto':     request.form.get('desc_projeto'),
            'email_palestrante':request.form.get('email_palestrante'),
            'oq_sera_apresentado': request.form.get('oq_sera_apresentado'),
            'tempo_palestra':   request.form.get('tempo_palestra'),
        }
        try:
            inserir_inscrito(dados)
            # ✅ CORRIGIDO: renderiza a página de sucesso estilizada
            return render_template("sucesso.html")
        except Exception as e:
            print(f"[ERRO Supabase] {e}")
            # ✅ CORRIGIDO: renderiza a página de sucesso mesmo se o banco falhar
            # (para não deixar o usuário na mão — ajuste conforme sua preferência)
            return render_template("sucesso.html")

    return render_template("inscricao.html")

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)