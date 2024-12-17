from flask import Flask
from config import Config
from db.db import db
from models import *
from routes import routes

def create_app():
    
    app = Flask(__name__)
    
    app.config.from_object(Config)  # Load database configuration
    db.init_app(app)  # Initialize database with Flask app
    
    with app.app_context():
        db.create_all()  # Create tables based on models 
        
    app.register_blueprint(routes.route_bp) #functionalities
    return app