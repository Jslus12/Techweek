from flask import Flask, render_template, request, abort
import psycopg2
import os

app = Flask(__name__, 
        template_folder='techweek-frontend/templates', 
        static_folder='techweek-frontend/static')

def get_db():
    return psycopg2.connect(os.environ.get('DATABASE_URL'))

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
    abort(404)

@app.route("/ajuda")
def ajuda(): 
    return render_template("ajuda.html")

@app.route("/inscricao", methods=['GET', 'POST'])
def inscricao():
    if request.method == 'POST':
        tipo            = request.form.get('tipo')
        nome            = request.form.get('nome')
        whatsapp        = request.form.get('whatsapp')
        ra              = request.form.get('ra')
        cafe            = request.form.get('cafe')
        curso_serie     = request.form.get('curso_serie')
        titulo_palestra = request.form.get('titulo_palestra')
        bio             = request.form.get('bio')

        try:
            conn = get_db()
            cursor = conn.cursor()
            query = """
                INSERT INTO inscritos 
                (tipo, nome_completo, whatsapp, ra, cafe, curso_serie, titulo_palestra, bio)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (tipo, nome, whatsapp, ra, cafe, curso_serie, titulo_palestra, bio))
            conn.commit()
            cursor.close()
            conn.close()
            return "Inscrição realizada com sucesso!"
        except Exception as e:
            return f"Erro ao gravar no banco: {e}"

    return render_template("inscricao.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))