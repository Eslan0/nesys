from flask import Blueprint, request, jsonify

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
    return jsonify({"message": error}), 409 # Conflict
  return jsonify({"message": "Usuario registrado com sucesso", "user_id": user.id}), 201
