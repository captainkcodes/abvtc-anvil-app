from ._anvil_designer import AccountTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Account(AccountTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    
  def getUserData(self):
    user = anvil.users.get_user(allow_remembered=True)
    email = self.item['email']
    if user:
      self.email_box.text = email
	
  def updateacct_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    user = anvil.users.get_user(allow_remembered=True)
    if (user):
      anvil.users.configure_account_with_form()

