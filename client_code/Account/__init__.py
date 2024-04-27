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
from ..Orders import Orders

class Account(AccountTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.getUserData()
    # Any code you write here will run before the form opens.
    
  def getUserData(self):
    users = anvil.users.get_user(allow_remembered=True)
    if users:
     user = anvil.server.call('getUserInfo').search()
     for userdata in user:
      self.email_box.text = userdata['email']
      self.pass_box.text = userdata['password_hash']
	
  def updateacct_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    user = anvil.users.get_user(allow_remembered=True)
    if (user):
      anvil.users.configure_account_with_form()

  def getOrders(self):
    order = anvil.server.call('getOrderInfo').search()
    for orders in order:
      c = Orders(orders['email'], orders['product'], orders['name'], orders['orderShipped'], orders['orderNumber'], orders['orderCreated'], orders['phoneNumber'])
      self.ordercontainer.add_component(c)