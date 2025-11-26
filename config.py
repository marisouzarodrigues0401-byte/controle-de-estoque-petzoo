import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        f"sqlite:///{os.path.join(BASE_DIR, 'inventory.db')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEFAULT_CITY = "Vargem Grande Paulista, SP"
    DEFAULT_RAIN_IMPACT = -0.3


def get_config():
    env = os.environ.get("FLASK_ENV", "development")
    return Config()
