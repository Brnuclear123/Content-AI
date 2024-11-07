import os
from flask import Flask, render_template, redirect, url_for, request, session, abort
from dotenv import load_dotenv
from jinja2 import ChoiceLoader, FileSystemLoader
from database import db, app  # Importa o app e db configurado no database.py
import models  # Importa os modelos para registrar as tabelas

app = Flask(__name__)

app.secret_key = "sua_chave_secreta"

# Configuração para múltiplas pastas de templates
app.jinja_loader = ChoiceLoader([
    FileSystemLoader('templates')
])

# Usuários de exemplo com tipos de acesso
users = {
    "dev": {"password": "1234", "role": "developer"},
    "client_user": {"password": "1234", "role": "client"}
}

# Decorador para verificar se o usuário está logado e tem o papel correto
def login_required(role=None):
    def wrapper(f):
        def decorated_function(*args, **kwargs):
            if 'role' not in session:
                return redirect(url_for('login'))
            if role and session['role'] != role:
                abort(403)  # Proibido
            return f(*args, **kwargs)
        decorated_function.__name__ = f.__name__
        return decorated_function
    return wrapper

# Rota principal que redireciona para a visão correta
@app.route('/')
def index():
    if 'role' in session:
        if session['role'] == 'developer':
            return redirect(url_for('dev_overview'))
        elif session['role'] == 'client':
            return redirect(url_for('client_overview'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)

        if user and user['password'] == password:
            session['username'] = username
            session['role'] = user['role']
            return redirect(url_for('index'))
        else:
            error = "Usuário ou senha incorretos."
            return render_template('login.html', error=error)
    
    return render_template('login.html')

# --------------------
# Rotas para Developer
# --------------------
@app.route('/index')
@login_required(role='developer')
def dev_overview():
    return render_template('index.html')

@app.route('/clients')
@login_required(role='developer')
def dev_clients():
    return render_template('clients.html')

@app.route('/system')
@login_required(role='developer')
def dev_system():
    return render_template('system.html')

@app.route('/moderation')
@login_required(role='developer')
def dev_moderation():
    return render_template('moderation.html')

@app.route('/analytics')
@login_required(role='developer')
def dev_analytics():
    return render_template('analytics.html')

@app.route('/content_ai')
@login_required(role='developer')
def dev_content_ai():
    return render_template('content_ai.html')

@app.route('/campaign')
@login_required(role='developer')
def dev_campaign():
    return render_template('campaign.html')

@app.route('/assets')
@login_required(role='developer')
def dev_assets():
    return render_template('assets.html')

@app.route('/company_profile')
@login_required(role='developer')
def dev_company_profile():
    return render_template('company_profile.html')

# --------------------
# Rotas para Client
# --------------------
@app.route('/client/overview')
@login_required(role='client')
def client_overview():
    return render_template('client_overview.html')

@app.route('/client/content_ai')
@login_required(role='client')
def client_content_ai():
    return render_template('client_content_ai.html')

@app.route('/client/campaign')
@login_required(role='client')
def client_campaign():
    return render_template('client_campaign.html')

@app.route('/client/assets')
@login_required(role='client')
def client_assets():
    return render_template('client_assets.html')

@app.route('/client/analytics')
@login_required(role='client')
def client_analytics():
    return render_template('client_analytics.html')

@app.route('/client/moderation')
@login_required(role='client')
def client_moderation():
    return render_template('client_moderation.html')

@app.route('/client/company_profile')
@login_required(role='client')
def client_company_profile():
    return render_template('client_company_profile.html')

# Rota de logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# Criar as tabelas antes da primeira requisição
@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
