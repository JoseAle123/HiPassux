from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://root:PASSWORD@localhost/Passux') #mysql://username:password@host:port/database_name
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', '1234')  # Cambia 'your_secret_key' por una clave secreta segura

    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', '1234')  # Cambia 'your_secret_key' por una clave secreta segura

    DEBUG = True