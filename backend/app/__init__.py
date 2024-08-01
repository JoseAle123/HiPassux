from flask import Flask
from app.extensions import db, migrate
from app.routes import init_routes
from app.config import Config
from app.api_routes import init_api_routes
from flask_jwt_extended import JWTManager

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Inicializa extensiones
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Inicializa rutas
    init_routes(app)
    init_api_routes(app)
    
    # Configura JWT
    jwt = JWTManager(app)

    jwt = JWTManager(app)
    
    return app

if __name__ == '__main__':
    app = create_app()
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"Error: {e}")
