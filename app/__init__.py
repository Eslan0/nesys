from flask import Flask, jsonify
from config import DevelopmentConfig, ProductionConfig

def create_app(config_class=DevelopmentConfig, config_name=None):
  app = Flask(__name__)
  app.config.from_object("config.Config")
  
  from .routes import user_routes, auth_routes, home_routes, product_routes, order_routes
  app.register_blueprint(user_routes.bp)
  app.register_blueprint(auth_routes.bp)
  app.register_blueprint(home_routes.bp)
  app.register_blueprint(product_routes.bp)
  app.register_blueprint(order_routes.bp)

  @app.errorhandler(404)
  def not_found_error(error):
    return jsonify({"message": "Recurso nao encontrado"}), 404

  @app.errorhandler(400)
  def bad_request_error(error):
    return jsonify({"message": "Requisição invalida"}), 400

  return app
