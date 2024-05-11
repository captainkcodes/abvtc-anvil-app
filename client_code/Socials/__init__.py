from ._anvil_designer import SocialsTemplate
from anvil import *
import anvil.server
import stripe.checkout
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users

from anvil.js.window import jQuery
from anvil.js import get_dom_node

class Socials(SocialsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    iframe = jQuery("<iframe width='100%' height='800px' style='border:solid 1px #777' frameborder='0' scrolling='no'>").attr("src", "https://calendar.google.com/calendar/embed?height=600&wkst=1&ctz=America%2FChicago&bgcolor=%23ffffff&src=cmVhbC5hYm92ZXRoZWNsb3Vkc0BnbWFpbC5jb20&src=YWRkcmVzc2Jvb2sjY29udGFjdHNAZ3JvdXAudi5jYWxlbmRhci5nb29nbGUuY29t&src=ZW4udXNhI2hvbGlkYXlAZ3JvdXAudi5jYWxlbmRhci5nb29nbGUuY29t&color=%23039BE5&color=%2333B679&color=%230B8043")
    iframe.appendTo(get_dom_node(self.calcontainer))
    # Any code you write here will run before the form opens.
