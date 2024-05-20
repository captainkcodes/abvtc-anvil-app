from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.users
from ..Landing import Landing
from ..Merch import Merch
from ..Socials import Socials
from ..Contact import Contact
from ..Profile import Profile

class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.container.add_component(Landing())
    self.logoutbtn.visible = False
    self.viewacctbtn.visible = False
    currentuser = anvil.users.get_user()
    if currentuser:
      self.logoutbtn.visible = True
      self.viewacctbtn.visible = True
      self.loginbtn.visible = False

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

  def viewacctbtn_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.container.clear()
    self.container.add_component(Profile())

  def loginbtn_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.login_with_form(show_signup_option=True, allow_cancel=True)
    currentuser = anvil.users.get_user()
    if currentuser:
      self.logoutbtn.visible = True
      self.viewacctbtn.visible = True
      self.loginbtn.visible = False
      Notification("Welcome to the Above the Clouds family!").show()

  def logoutbtn_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.logout(invalidate_client_objects=False)
    currentuser = anvil.users.get_user()
    if currentuser:
      self.logoutbtn.visible = False
      self.viewacctbtn.visible = False
      self.loginbtn.visible = True
      Notification("Logout successful! Come back soon!").show()
