import sys
import flask

from lib import biblioteca_filme

print('filme')

__filme__ = "filme_app"
app = flask.Flask(__filme__)

# Parametrii globali pentru descriere si recenzii

@app.route("/", methods=['GET'])
def index():
    ret = """
    <html>
    <head>
        <title>Filme</title>
        <link href="https://fonts.googleapis.com/css2?family=Roboto+Slab:wght@400;700&display=swap" rel="stylesheet">
        <style>
            body {
                font-family: 'Roboto Slab', serif;
                margin: 0;
                padding: 0;
                background-color: #1c1c1c;
                color: #f0f0f0;
            }
            header {
                background-color: #8b0000;
                color: #f0f0f0;
                padding: 20px 0;
                text-align: center;
            }
            h1 {
                margin: 0;
                font-weight: 700;
                text-transform: uppercase;
                letter-spacing: 2px;
            }
            nav {
                margin: 30px;
                text-align: center;
            }
            nav a {
                margin: 0 15px;
                text-decoration: none;
                color: #8b0000;
                font-weight: 700;
                transition: color 0.3s;
            }
            nav a:hover {
                color: #f0f0f0;
            }
            .container {
                padding: 30px;
                background-color: #333;
                margin: 30px auto;
                width: 80%;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                border-radius: 5px;
                animation: fade-in 1s;
            }
            @keyframes fade-in {
                from { opacity: 0; }
                to { opacity: 1; }
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Film</h1>
        </header>
        <nav>
            <a href="/">Acasă</a>
            <a href="/descriere/the-lighthouse">Descriere</a>
            <a href="/recenzii/the-lighthouse">Recenzii</a>
        </nav>
        <div class="container">
        Pagina Principala a Aplicatiei Web.
        </div>
    </body>
    </html>
    """
    return ret

@app.route("/descriere/the-lighthouse", methods=['GET'])
def get_descriere():
    descriere=biblioteca_filme.descriere_film()
    return descriere

@app.route("/recenzii/the-lighthouse", methods=['GET'])
def get_recenzii():
    recenzii=biblioteca_filme.recenzii_film()
    return recenzii

@app.cli.command()
def test():
    """
    Rulare 'unit tests'

    Apelare pytest din aplicatia systest, cu ajutorul comenzii flask.
    """
    import pytest
    errno = pytest.main(["-x", "app/test"])
    sys.exit(errno)

if __name__ == "__main__":
    app.run()