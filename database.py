# database.py
import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask import Flask

# Carregar configurações do .env
load_dotenv()

# Configuração do Flask
app = Flask(__name__)

# Configuração do Banco de Dados
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

# String de conexão com o banco de dados MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar SQLAlchemy
db = SQLAlchemy(app)
