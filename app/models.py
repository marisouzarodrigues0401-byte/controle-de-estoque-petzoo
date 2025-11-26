from datetime import datetime
from . import db


class TimestampMixin:
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class AppSettings(db.Model, TimestampMixin):
    __tablename__ = "app_settings"

    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(120), nullable=False)
    weather_provider = db.Column(db.String(50), default="openweathermap")
    api_key = db.Column(db.String(120), nullable=True)
    rain_impact_factor = db.Column(db.Float, default=-0.3)
    sunny_message = db.Column(db.String(255), default="Tempo bom — movimento normal ou alto esperado.")
    rain_message = db.Column(db.String(255), default="Previsão de chuva — movimento de visitantes pode cair.")

    def as_dict(self):
        return {
            "id": self.id,
            "city": self.city,
            "weather_provider": self.weather_provider,
            "api_key": self.api_key,
            "rain_impact_factor": self.rain_impact_factor,
            "sunny_message": self.sunny_message,
            "rain_message": self.rain_message,
        }


class Item(db.Model, TimestampMixin):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    categoria = db.Column(db.String(120), nullable=True)
    unidade = db.Column(db.String(60), nullable=True)
    estoque_atual = db.Column(db.Integer, default=0)
    estoque_minimo = db.Column(db.Integer, default=0)
    observacoes = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<Item {self.nome}>"
