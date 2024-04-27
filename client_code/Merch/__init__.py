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
from ..Product import Product

class Merch(MerchTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.loadProducts()

    # Any code you write here will run before the form opens.

  
  def loadProducts(self):
    products = anvil.server.call('getProductInfo').search()
    product_panel = GridPanel()
    for i, product in enumerate(products):
      c = Product(variant=product['variant'], button_text=f"Purchase for ${product['retailPrice']}", description=product['description'], image=product['image'], button_callback=None)
      product_panel.add_component(c, row=str(i//2), col_xs=6)
      self.container.add_component(product_panel)
      

      
