from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/campaign')
def campaign():
    return render_template('campaign.html')

@app.route('/clients')
def clients():
    return render_template('clients.html')

@app.route('/system')
def system():
    return render_template('system.html')

@app.route('/moderation')
def moderation():
    return render_template('moderation.html')

@app.route('/analytics')
def analytics():
    return render_template('analytics.html')

@app.route('/assets')
def assets():
    return render_template('assets.html')

@app.route('/content-ai')
def content_ai():
    return render_template('content_ai.html')

if __name__ == '__main__':
    app.run(debug=True)
