from flask import Flask, render_template, redirect, url_for, request, session, abort
from jinja2 import ChoiceLoader, FileSystemLoader

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

@app.route('/')
def index():
    if 'role' in session:
        if session['role'] == 'developer':
            return render_template('index.html')
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

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# Rota para moderação, com distinção entre desenvolvedores e clientes
@app.route('/moderation')
@login_required()
def moderation():
    if session['role'] == 'developer':
        return render_template('moderation.html')  # Moderation global
    elif session['role'] == 'client':
        return render_template('client_moderation.html')  # Moderation para cliente

# Rota de analytics, separada para desenvolvedores e clientes
@app.route('/analytics')
@login_required()
def analytics():
    if session['role'] == 'developer':
        return render_template('analytics.html')
    elif session['role'] == 'client':
        return render_template('client_analytics.html')

# Rota específica para desenvolvedores - Clients
@app.route('/clients')
@login_required(role='developer')
def clients():
    return render_template('clients.html')

# Rota específica para desenvolvedores - System
@app.route('/system')
@login_required(role='developer')
def system():
    return render_template('system.html')

# Rota de campanhas, acessível para todos os usuários logados
@app.route('/campaign')
@login_required()
def campaign():
    if session['role'] == 'developer':
        return render_template('campaign.html')
    elif session['role'] == 'client':
        return render_template('client_campaign.html')

# Biblioteca de ativos, acessível para todos os usuários logados
@app.route('/assets')
@login_required()
def assets():
    if session['role'] == 'developer':
        return render_template('assets.html')
    elif session['role'] == 'client':
        return render_template('client_assets.html')

# Content AI, acessível para todos os usuários logados
@app.route('/content_ai')
@login_required()
def content_ai():
    if session['role'] == 'developer':
        return render_template('content_ai.html')
    elif session['role'] == 'client':
        return render_template('client_content_ai.html')

# Perfil da empresa, acessível para todos os usuários logados
@app.route('/company_profile')
@login_required()
def company_profile():
    if session['role'] == 'developer':
        return render_template('company_profile.html')
    elif session['role'] == 'client':
        return render_template('client_company_profile.html')

# Rota de visão geral específica para o cliente
@app.route('/client_overview')
@login_required(role='client')
def client_overview():
    return render_template('client_overview.html')

if __name__ == '__main__':
    app.run(debug=True)
