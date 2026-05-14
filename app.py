from flask import Flask, render_template, request, abort, redirect, url_for, session
import os
import urllib.request
import json

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

app.secret_key = 'techweek2026secretkey'
DASHBOARD_USER = 'crisloginteste'
DASHBOARD_PASS = 'K9!vQ#72Lp@zR4mX'

SUPABASE_URL = os.environ.get('SUPABASE_URL', '')
SUPABASE_KEY = os.environ.get('SUPABASE_KEY', '')

def inserir_inscrito(dados):
    if not SUPABASE_URL or not SUPABASE_KEY:
        return
    url = f"{SUPABASE_URL}/rest/v1/inscritos"
    body = json.dumps(dados).encode('utf-8')
    req = urllib.request.Request(url, data=body, method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('apikey', SUPABASE_KEY)
    req.add_header('Authorization', f'Bearer {SUPABASE_KEY}')
    req.add_header('Prefer', 'return=minimal')
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

PALESTRANTES_DADOS = {
    'gustavo-melles': {
        'nome': 'Gustavo Melles',
        'trilha': '01/06 · SEGUNDA · 19:15',
        'sub_titulo': 'Pense com IA: A Revolução da Inteligência Ampliada',
        'imagem': 'Gustavo Melles.png',
        'descricao_completa': """
            <p>Graduação em Publicidade e Marketing pela Mackenzie. Fundador do portal
            <strong>BuscaIA.com</strong> e da <strong>OiRobo.com</strong>.</p>
            <p>Professor no MBA em Inovação e Inteligência Artificial para Negócios da PUCPR
            e Colunista na Rádio CBN Londrina.</p>
            <p>Atuação em grandes marcas como Bayer, Toyota, Uber, Cielo, Natura e Unimed,
            além de projetos no setor de entretenimento, como os shows U2 360 e Cirque du Soleil.</p>
        """
    },
    'jessy-ferracioli': {
        'nome': 'Jessy Borges Ferracioli',
        'trilha': '01/06 · SEGUNDA · 20:30',
        'sub_titulo': 'Os data taggers e o trabalho invisível por trás da Inteligência Artificial',
        'imagem': 'jessy.png',
        'descricao_completa': """
            <p>Advogada há mais de 10 anos, atualmente advoga em uma empresa do ramo de
            licitações públicas.</p>
            <p>Pós-graduada em Direito Civil e Processo Civil pelo IDCC — Instituto de Direito
            Constitucional e Cidadania. Mestrado em Direito, Sociedades e Tecnologias pelas
            Faculdades Londrina.</p>
            <p>Pesquisadora de direito e inteligência artificial na <strong>Lawgorithm</strong>,
            do núcleo IA e Raça.</p>
        """
    },
    'luciano-soler': {
        'nome': 'Luciano Soler',
        'trilha': '02/06 · TERÇA · 19:15',
        'sub_titulo': 'Construção e Orquestração de Agentes de IA',
        'imagem': 'luciano.png',
        'descricao_completa': """
            <p>Engenheiro da Computação, Especialista em Engenharia de Software e
            Mestre em Ciências da Computação.</p>
            <p>Atualmente trabalha com desenvolvimento de Software e IA no
            <strong>Instituto Agronômico do Paraná – IAPAR</strong>.</p>
        """
    },
    'michel-banagouro': {
        'nome': 'Michel Cesar Leme Banagouro',
        'trilha': '02/06 · TERÇA · 20:30',
        'sub_titulo': 'O programador morreu. Vida longa ao programador',
        'imagem': 'michel.png',
        'descricao_completa': """
            <p>Arquiteto de Software e <strong>CTO na Leanwork Group</strong>. Formado em
            Análise e Desenvolvimento de Sistemas com 20 anos de experiência na área.</p>
            <p>Atuou no desenvolvimento e liderança técnica de grandes e-commerces como
            <strong>Centauro, Ultrafarma e Riachuelo</strong>.</p>
        """
    },
    'luiz-nunes': {
        'nome': 'Luiz Fernando Pereira Nunes',
        'trilha': '03/06 · QUARTA · 19:15',
        'sub_titulo': 'Inteligência Artificial e Proteção de Dados: Desafios, Ética e Segurança na Era Digital',
        'imagem': 'luiz.png',
        'descricao_completa': """
            <p>Profissional da área de tecnologia com mais de 15 anos de experiência em
            Gerenciamento de Projetos, atuando em empresas de médio e grande porte,
            nacionais e multinacionais, nos setores de tecnologia, agronegócio, educação,
            jurídico e infraestrutura.</p>
            <p>Graduado em Ciência da Computação, MBA em Gestão de Projetos, Estratégia
            Empresarial e Gestão Comercial. Mestrado em Ciência da Computação na
            <strong>Universidade Estadual de Londrina</strong> e Mestrado em Direito e Tecnologia.</p>
            <p>Líder na <strong>Hanke Digital Solutions</strong>, gerencia produtos, projetos
            e times ágeis com foco em resultado, melhoria contínua e formação de lideranças.</p>
        """
    },
}

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
            'tipo':                 request.form.get('tipo'),
            'nome_completo':        request.form.get('nome'),
            'whatsapp':             request.form.get('whatsapp'),
            'ra':                   request.form.get('ra'),
            'cafe': 'Sim' if request.form.get('cafe') else 'Nao',
            'curso_serie':          request.form.get('curso_serie'),
            'titulo_palestra':      request.form.get('titulo_palestra'),
            'bio':                  request.form.get('bio'),
            'nome_projeto':         request.form.get('nome_projeto'),
            'desc_projeto':         request.form.get('desc_projeto'),
            'email_palestrante':    request.form.get('email_palestrante'),
            'oq_sera_apresentado':  request.form.get('oq_sera_apresentado'),
            'tempo_palestra':       request.form.get('tempo_palestra'),
        }
        try:
            inserir_inscrito(dados)
            return render_template("sucesso.html")
        except Exception as e:
            return render_template("sucesso.html")
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
        palestrantes_count = len([x for x in todos if x.get('tipo') == 'palestrante'])
        cafe = len([x for x in todos if x.get('cafe') == 'Sim'])
        projetos = len([x for x in todos if x.get('nome_projeto')])
        return render_template("dashboard.html",
            total=total,
            alunos=alunos,
            palestrantes=palestrantes_count,
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
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)