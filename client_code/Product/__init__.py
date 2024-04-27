from ._anvil_designer import ProductTemplate
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


class Product(ProductTemplate):
  def __init__(self, variant, description, button_text, image, button_callback, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.prodname.text = variant
    self.proddescription.text = description
    self.buybtn.text = button_text
    self.image_content.source = image
    
    # Any code you write here will run before the form opens.
