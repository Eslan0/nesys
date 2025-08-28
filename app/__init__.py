import os
from flask import Flask, jsonify
from config import DevelopmentConfig, ProductionConfig

def create_app(config_class=DevelopmentConfig, config_name=None):
  # Define o caminho absoluto para o diretório 'app'
  app_dir = os.path.dirname(os.path.abspath(__file__))
  
  # Define o caminho para o diretório 'templates' dentro do 'app'
  template_dir = os.path.join(app_dir, 'templates')
  
  # Passa o caminho da pasta de templates para a instância do Flask
  app = Flask(__name__, template_folder=template_dir)
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
