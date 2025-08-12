from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    from app.views.products import products_bp
    app.register_blueprint(products_bp)

    return app
