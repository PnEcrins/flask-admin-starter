from flask import Flask, request

from app.config.config import config
from flask_babel import Babel
from flask_migrate import Migrate


from app.env import db
from app.admin import admin


def get_locale():
    return request.accept_languages.best_match(['de', 'fr', 'en'])


def create_app():
    app = Flask(__name__)
    app.config.update(config)
    app.config["FLASK_ADMIN_FLUID_LAYOUT"] = True
    db.init_app(app)
    with app.app_context():
        db.create_all()
    admin.init_app(app)
    babel = Babel(app, locale_selector=get_locale)

    migrate = Migrate(app, db)
    from app.blueprint import routes

    app.register_blueprint(routes)
    return app


