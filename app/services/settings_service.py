from typing import Optional
from flask import current_app
from .. import db
from ..models import AppSettings


def ensure_default_settings() -> AppSettings:
    settings = AppSettings.query.first()
    if settings:
        return settings

    config = current_app.config
    settings = AppSettings(
        city=config.get("DEFAULT_CITY", "São Paulo, SP"),
        rain_impact_factor=config.get("DEFAULT_RAIN_IMPACT", -0.3),
    )
    db.session.add(settings)
    db.session.commit()
    return settings


def get_settings() -> AppSettings:
    settings = AppSettings.query.first()
    if not settings:
        settings = ensure_default_settings()
    return settings


def update_settings(**kwargs) -> AppSettings:
    settings = get_settings()
    for field, value in kwargs.items():
        if hasattr(settings, field) and value is not None:
            setattr(settings, field, value)
    db.session.commit()
    return settings
