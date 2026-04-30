from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__, 
        template_folder='techweek-frontend/templates', 
        static_folder='techweek-frontend/static')

# Configuração da conexão com o banco de dados do Laragon
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='', # Padrão do Laragon é vazio
        database='teckweek_db' # Nome que você criou no HeidiSQL
    )

@app.route("/")
def index():
    return render_template("index.html")

# Rota de inscrição atualizada para salvar no banco
@app.route("/inscricao", methods=['GET', 'POST'])
def inscricao():
    if request.method == 'POST':
        # Pega os dados vindos do formulário HTML
        nome = request.form.get('nome')
        email = request.form.get('email')

        # Salva no MySQL
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO participantes (nome, email) VALUES (%s, %s)', (nome, email))
        conn.commit()
        cursor.close()
        conn.close()

        return "<h1>Inscrição realizada com sucesso!</h1><a href='/'>Voltar</a>"
    
    return render_template("inscricao.html")

# Outras rotas permanecem iguais
@app.route("/devs")
def devs(): return render_template("devs.html")

@app.route("/palestrantes")
def palestrantes(): return render_template("palestrantes.html")

@app.route("/ajuda")
def ajuda(): return render_template("ajuda.html")

if __name__ == "__main__":
    app.run(debug=True)