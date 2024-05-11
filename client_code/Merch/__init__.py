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
#from ..Home import Home
from ..Account import Account
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

    
   # self.loadProducts()

    self.logout_btn.visible = False
    self.viewacct_btn.visible = False
    user = anvil.users.get_user(allow_remembered=True)
    if user:
      self.logout_btn.visible = True
      self.viewacct_btn.visible = True
      self.login_btn.visible = False
    # Any code you write here will run before the form opens.

  
 # def loadProducts(self):
  #  products = anvil.server.call('getProductInfo').search()
    #product_panel = GridPanel()
  #  for product in products:
   #   c = Product(variant=product['variant'], button_text=f"Purchase for ${product['retailPrice']}", description=product['description'], image=product['image'], button_callback=None, size=product['size'], color=product['color'])
      #product_panel.add_component(c, row=str(i//2), col_xs=6)
   #   self.container.add_component(c)

  def home_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.container.clear()
    #open_form('Home')

  def social_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.container.clear()
    self.container.add_component(Socials())

  def merch_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.container.clear()
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
    open_form('Home')

  def viewacct_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.container.clear()
    self.container.add_component(Account())

