import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.stripe
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.server
from datetime import datetime

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
@anvil.server.callable
def send_feedback(name, email, comment):
  #send yourself an email each time a comment is submitted
  anvil.email.send(from_name="Abvtc Support", to="idasha.glenn7@gmail.com", subject=f"Comment from {name}", text=f"""
  
  A new person has submitted a comment in the contact us form!
  
  Name: {name}
  Email address: {email}
  Comment:
  {comment}
  """)
  app_tables.comments.add_row(
    name=name,
    email=email,
    comment=comment,
    created=datetime.now()
  )

