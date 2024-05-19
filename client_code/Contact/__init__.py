from ._anvil_designer import ContactTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.users


class Contact(ContactTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def submit_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    name = self.name_box.text
    email = self.email_box.text
    comment = self.comment_box.text
    anvil.server.call('send_feedback', name, email, comment)
    Notification("Comment submitted!").show()
    self.clear_inputs()


  def clear_inputs(self):
    self.name_box.text = ""
    self.email_box.text = ""
    self.comment_box.text = ""
