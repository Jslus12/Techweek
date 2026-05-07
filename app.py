from flask import Flask, render_template, abort

app = Flask(__name__, 
        template_folder='techweek-frontend/templates', 
        static_folder='techweek-frontend/static')

# Baseado nos arquivos que vi na sua pasta static/Img
dados_palestrantes = {
    'bruno': {
        'nome': 'Bruno Silva',
        'trilha': '>> IA & DADOS',
        'sub_titulo': 'Especialista em Visão Computacional',
        'imagem': 'bruno.jpg', 
        'descricao_completa': '<p>Descrição detalhada do Bruno aqui...</p>'
    },
    'heitor': {
        'nome': 'Heitor Santos',
        'trilha': '>> DESENVOLVIMENTO',
        'sub_titulo': 'Arquiteto de Software',
        'imagem': 'heitor.jpeg',
        'descricao_completa': '<p>Descrição detalhada do Heitor aqui...</p>'
    },
    'jao': {
        'nome': 'João Silva',
        'trilha': '>> CLOUD COMPUTING',
        'sub_titulo': 'Expert em AWS',
        'imagem': 'jao.jpg',
        'descricao_completa': '<p>Descrição detalhada do João aqui...</p>'
    }
}

@app.route("/")
def index(): return render_template("index.html")

@app.route("/devs")
def devs(): return render_template("devs.html")

@app.route("/palestrantes")
def palestrantes(): return render_template("palestrantes.html")

@app.route("/perfil/<nome_url>")
def perfil(nome_url):
    palestrante = dados_palestrantes.get(nome_url.lower())
    if not palestrante:
        abort(404)
    return render_template("perfil.html", palestrante=palestrante)

@app.route("/ajuda")
def ajuda(): return render_template("ajuda.html")

@app.route("/inscricao")
def inscricao(): return render_template("inscricao.html")

if __name__ == "__main__":
    app.run(debug=True)