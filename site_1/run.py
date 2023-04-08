from flask import Flask
from flask import render_template
from flask_wtf.csrf import CSRFProtect
from views import main
import os

# Inicializa a aplicação Flask

app = Flask(__name__)
app.static_folder = 'static'
app.static_url_path = '/static'

csrf = CSRFProtect(app)
@app.route('/')
def index():
    return render_template('index.html')

# Importa as rotas da aplicação
app.register_blueprint(main)

app.run(debug=True)