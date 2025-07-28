from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name=None):
    app = Flask(__name__)
    
    # Load configuration
    if config_name:
        app.config.from_object(f'app.config.{config_name}')
    else:
        app.config.from_object('app.config.Config')
    
    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Import models
    from app import models
    
    # Register blueprints/routes
    from app import routes
    app.register_blueprint(routes.bp)
    
    return app

# Create app instance for direct import
app = create_app()