from ._anvil_designer import MerchTemplate
from anvil import *
import anvil.server
import stripe.checkout
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
from ..Socials import Socials

#trying something
from anvil.js.window import jQuery
from anvil.js import get_dom_node

class Merch(MerchTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    iframe = jQuery("<iframe width='100%' height='800px'>").attr("src", "https://shirtcrafters.square.site/")
    iframe.appendTo(get_dom_node(self.container))

    # Any code you write here will run before the form opens.
