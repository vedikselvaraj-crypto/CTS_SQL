"""
================================================================================
FLASK APPLICATION FACTORY (app.py)
================================================================================
Instantiates the Flask application using Application Factory pattern (create_app).
Registers configuration, blueprints, and global JSON error handlers.
================================================================================
"""

from flask import Flask, jsonify
from config import Config
from courses.routes import courses_bp


def create_app() -> Flask:
    """Application Factory Function."""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register Blueprints
    app.register_blueprint(courses_bp)

    # --------------------------------------------------------------------------
    # GLOBAL JSON ERROR HANDLERS (Ensures API never returns HTML error pages)
    # --------------------------------------------------------------------------
    @app.errorhandler(404)
    def handle_not_found(error):
        return jsonify({
            "status": "error",
            "code": 404,
            "message": "Resource or endpoint not found"
        }), 404

    @app.errorhandler(500)
    def handle_internal_error(error):
        return jsonify({
            "status": "error",
            "code": 500,
            "message": "Internal Server Error"
        }), 500

    @app.route('/')
    def root_health():
        return jsonify({"message": "Flask Course Management API is active"}), 200

    return app


if __name__ == '__main__':
    app = create_app()
    print("[INFO] Starting Flask Development Server on port 5000...")
    app.run(host='0.0.0.0', port=5000, debug=True)
