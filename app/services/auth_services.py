from flask import jsonify
from app.models import User

class AuthService:
  @staticmethod
  def register_user(username, email, password):
    user = User(username=username, email=email, password=password)
    try:
      user.save()
      return user, None
    except Exception as e:
      return None, str(e)

  @staticmethod
  def login_user(email, password):
    user = User.query.filter_by(email=email).first()
    if user and user.password == password:
      return user, None
    return None, "Credenciais inválidas"

  @staticmethod
  def logout_user():
    return 

  @staticmethod
  def update_user(user):
    try:
      user.save()
      return user, None
    except Exception as e:
      return None, str(e)

  @staticmethod
  def delete_user(user):
    try:
      user.delete()
      return user, None
    except Exception as e:
      return None, str(e)

  @staticmethod
  def get_user(user_id):
    user = User.query.get(user_id)
    if user:
      return user, None
    return None, "Usuário nao encontrado"

  @staticmethod
  def get_all_users():
    users = User.query.all()
    return users, None
