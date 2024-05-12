from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import stripe.checkout
import anvil.server
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
from ..Landing import Landing
from ..Merch import Merch
from ..Socials import Socials
from ..Contact import Contact

class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.container.add_component(Landing())

  def home_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.container.clear()
    self.container.add_component(Home())

  def social_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.container.clear()
    self.container.add_component(Socials())

  def merch_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.container.clear()
    self.container.add_component(Merch())

  def contact_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.container.clear()
    self.container.add_component(Contact())
