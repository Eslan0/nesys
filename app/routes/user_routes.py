from flask import Blueprint, render_template

bp = Blueprint("users", __name__)

@bp.route("/users")
def list_products():
  return render_template("users/users.html")