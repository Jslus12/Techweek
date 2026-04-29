from flask import Flask, render_template

app = Flask(__name__, 
        template_folder='techweek-frontend/templates', 
        static_folder='techweek-frontend/static')



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/devs")
def devs():
    return render_template("devs.html")

@app.route("/palestrantes")
def palestrantes():
    return render_template("palestrantes.html")

@app.route("/ajuda")
def ajuda():
    return render_template("ajuda.html")

@app.route("/inscricao")
def inscricao():
    return render_template("inscricao.html")

if __name__ == "__main__":
    app.run(debug=True)