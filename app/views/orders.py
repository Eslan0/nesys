from flask import Blueprint, render_template

orders_bp = Blueprint("orders", __name__)

@orders_bp.route("/orders")
def list_products():
  return render_template("orders.html")