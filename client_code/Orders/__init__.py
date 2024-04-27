from ._anvil_designer import OrdersTemplate
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


class Orders(OrdersTemplate):
  def __init__(self, ordemail, ordprod, ordname, ordship, ordnum, ordcreated, ordphnum, ordershipstat, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.emailused_box.text = ordemail
    self.prodordered_box.text = ordprod
    self.nameorder_box.text = ordname
    self.shipadd_box.text = ordship
    self.ordnum_box = ordnum
    self.ordcreate_box = ordcreated
    self.phone_box = ordphnum
    self.shipstat_box = ordershipstat

    # Any code you write here will run before the form opens.
