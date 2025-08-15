from flask import Blueprint, render_template

bp = Blueprint("products", __name__)

@bp.route("/products")
def list_products():
  return render_template("products/products.html")