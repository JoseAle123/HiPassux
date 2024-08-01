from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Inicialización de extensiones
db = SQLAlchemy()
migrate = Migrate()


# Aquí podrías inicializar otras extensiones, por ejemplo:
# from flask_login import LoginManager
# login_manager = LoginManager()
