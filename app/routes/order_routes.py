from flask import Blueprint, render_template

bp = Blueprint("orders", __name__)

@bp.route("/orders")
def list_products():
  return render_template("orders/orders.html")