#from flask_sqlalchemy import SQLAlchemy

#db = SQLAlchemy()

class User:
  def __init__(self, username, email, password):
    self.username = username
    self.email = email
    self.password = password

  def save(self):
    pass

  def delete(self):
    pass

  def update(self):
    pass

class Order:
  def __init__(self, user_id, product_id, quantity):
    self.user_id = user_id
    self.product_id = product_id
    self.quantity = quantity

  def save(self):
    pass

  def delete(self):
    pass

  def update(self):
    pass

class Product:
  def __init__(self, name, description, price):
    self.name = name
    self.description = description
    self.price = price

  def save(self):
    pass

  def delete(self):
    pass

  def update(self):
    pass

class OrderItem:
  def __init__(self, order_id, product_id, quantity):
    self.order_id = order_id
    self.product_id = product_id
    self.quantity = quantity

  def save(self):
    pass

  def delete(self):
    pass

  def update(self):
    pass