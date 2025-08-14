from flask import Flask, jsonify
from config import DevelopmentConfig, ProductionConfig
from app.views.home import home_bp
from app.views.auth import auth_bp
from app.views.users import users_bp
from app.views.products import products_bp
from app.views.orders import orders_bp

def create_app(config_class=DevelopmentConfig):
  app = Flask(__name__)
  app.config.from_object("config.Config")

  app.register_blueprint(home_bp, url_prefix="/api/v1.2.0")
  app.register_blueprint(auth_bp, url_prefix="/api/v1.2.0")
  app.register_blueprint(users_bp, url_prefix="/api/v1.2.0")
  app.register_blueprint(products_bp, url_prefix="/api/v1.2.0")
  app.register_blueprint(orders_bp, url_prefix="/api/v1.2.0")

  @app.errorhandler(404)
  def not_found_error(error):
    return jsonify({"message": "Recurso nao encontrado"}), 404

  @app.errorhandler(400)
  def bad_request_error(error):
    return jsonify({"message": "Requisição invalida"}), 400

  return app
