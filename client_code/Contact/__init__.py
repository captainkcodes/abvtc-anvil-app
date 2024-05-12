from ._anvil_designer import ContactTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import stripe.checkout
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users


class Contact(ContactTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def submit_button_click(self, **event_args):
    #Set 'name' to the text in the 'name_box'
    name = self.name_box.text
    #set 'email' to the text in the 'email_box'
    email = self.email_box.text
    #set 'feedback' to the text in the 'feedback_box'
    feedback = self.feedback_box.text
    anvil.server.call('send_feedback', name, email, feedback)
    Notification("Feedback submitted!").show()
    self.clear_inputs()

  def clear_inputs(self):
    #clear our three text boxes
    self.name_box.text = ""
    self.email_box.text = ""
    self.feedback_box.text = ""