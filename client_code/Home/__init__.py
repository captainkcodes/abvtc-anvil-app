from ._anvil_designer import HomeTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
from ..Landing import Landing
from ..Account import Account
from ..Merch import Merch
from ..Socials import Socials


class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.container.add_component(Landing())
    self.logout_btn.visible = False
    self.viewacct_btn.visible = False
    user = anvil.users.get_user(allow_remembered=True)
    if user:
      self.logout_btn.visible = True
      self.viewacct_btn.visible = True
      self.login_btn.visible = False

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
    self.container.remove_from_parent()
    self.container.add_component(Merch())

  def login_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.login_with_form(show_signup_option=True, allow_cancel=True)
    
    user = anvil.users.get_user(allow_remembered=True)
    if (user):
      self.logout_btn.visible = True
      self.login_btn.visible = False
      self.viewacct_btn.visible = True
      alert("Welcome back!")
    elif (anvil.users.EmailNotConfirmed()):
      Notification("Please come back when you confirm your email! Check your spam folders!!", style="info", timeout=4)

  def logout_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.logout()
    alert("Log out successful! See you soon.")
    self.logout_btn.visible = False
    self.login_btn.visible = True
    self.viewacct_btn.visible = False

  def viewacct_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.container.clear()
    self.container.add_component(Account())

    