from ._anvil_designer import MerchTemplate
from anvil import *
import anvil.server
import stripe.checkout
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Merch(MerchTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.loadProducts()

    # Any code you write here will run before the form opens.

  def loadProducts(self):
    products = anvil.server.call('getProductInfo').search()
    
    for product in products:
      print(product["variant"])
