from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import get_config


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(get_config())

    db.init_app(app)

    from . import models  # noqa: F401 ensure models imported
    from .routes import main_bp

    app.register_blueprint(main_bp)

    @app.cli.command("init-db")
    def init_db_command():
        """Inicializa o banco com registros padrão."""
        from .services.settings_service import ensure_default_settings

        with app.app_context():
            db.create_all()
            ensure_default_settings()
            print("Banco inicializado com sucesso!")

    return app
