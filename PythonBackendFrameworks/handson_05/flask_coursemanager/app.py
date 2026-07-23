"""
================================================================================
FLASK APPLICATION FACTORY WITH FLASK-MIGRATE (app.py)
================================================================================
"""

from flask import Flask, jsonify
from flask_migrate import Migrate
from config import Config
from database import db
import models  # Ensure models are imported for SQLAlchemy metadata
from courses.routes import courses_bp


def create_app() -> Flask:
    """Application Factory Function."""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize SQLAlchemy database & Flask-Migrate
    db.init_app(app)
    Migrate(app, db)

    # Register Blueprints
    app.register_blueprint(courses_bp)

    @app.errorhandler(404)
    def handle_not_found(error):
        return jsonify({"status": "error", "code": 404, "message": "Resource not found"}), 404

    @app.errorhandler(500)
    def handle_server_error(error):
        return jsonify({"status": "error", "code": 500, "message": "Internal Server Error"}), 500

    @app.route('/')
    def root():
        return jsonify({"message": "Flask SQLAlchemy Course Management Engine Active"}), 200

    return app


if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    print("[INFO] Starting Flask Server on port 5000...")
    app.run(host='0.0.0.0', port=5000, debug=True)
