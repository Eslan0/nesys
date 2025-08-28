
from flask import Blueprint, render_template, request, jsonify
from app.services.auth_services import AuthService

bp = Blueprint("auth", __name__)

@bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not all([username, email, password]):
        return jsonify({"message": "Dados incompletos."}), 400

    user, error = AuthService.register_user(username, email, password)
    if error:
        return jsonify({"message": error}), 409
    return jsonify({"message": "Usuário registrado com sucesso", "user_id": user.id}), 201

@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("auth/login.html")

    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not all([email, password]):
        return jsonify({"message": "Dados incompletos."}), 400

    user, error = AuthService.login_user(email, password)
    if error:
        return jsonify({"message": error}), 401
    return jsonify({"message": "Login realizado com sucesso", "user_id": user.id}), 200

@bp.route("/logout", methods=["POST"])
def logout():
  return jsonify({"message": "Logout realizado com sucesso"}), 200