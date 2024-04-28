import anvil.stripe
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


@anvil.server.callable
def getProductInfo():
  #returns data that clients can read but not modify
  return app_tables.products.client_readable()

@anvil.server.callable
def getUserInfo():
  #returns data from user table
  user = anvil.users.get_user(allow_remembered=True)
  if user:
   return app_tables.users.client_readable()

@anvil.server.callable
def updateUserInfo():
  #returns data from user table and allows for updates
  return app_tables.users.client_writable()

@anvil.server.callable
def getOrderInfo():
  return app_tables.orders.client_readable()