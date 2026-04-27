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

if __name__ == "__main__":
    app.run(debug=True)