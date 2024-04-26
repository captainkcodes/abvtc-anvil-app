from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
from ..Landing import Landing

class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.container.add_component(Landing())
    self.logout_btn.visible = False
    self.viewacct_btn.visible = False

  def home_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Home')

  def social_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Socials')

  def merch_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Merch')

  def login_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.login_with_form(show_signup_option=True, allow_cancel=True)
    
    user = anvil.users.get_user(allow_remembered=True)
    if (user):
      self.logout_btn.visible = True
      self.login_btn.visible = False
      self.viewacct_btn.visible = True
      alert("Welcome back!", dismissible=True)
    elif (anvil.users.EmailNotConfirmed()):
      Notification("Please come back when you confirm your email! Check your spam folders!!", style="info", timeout=4)

  def logout_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.logout()
    alert("Log out successful! See you soon.", dismissible=True)
    user = anvil.users.get_user(allow_remembered=True)
    if (user):
      self.logout_btn.visible = False
      self.login_btn.visible = True
      self.viewacct_btn.visible = False

  def viewacct_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.container.add_component(Account())

    