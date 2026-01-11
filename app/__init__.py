from flask import Flask

def create_app():
    """Factory function para crear y configurar la aplicación Flask"""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev-secret-key-change-in-production'
    
    # Registrar blueprints/rutas
    from app.routes import main
    app.register_blueprint(main)
    
    return app

