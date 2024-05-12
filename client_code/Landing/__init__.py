from ._anvil_designer import LandingTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import stripe.checkout
import anvil.server
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users

from anvil.js.window import jQuery
from anvil.js import get_dom_node

class Landing(LandingTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    iframe = jQuery("<iframe width='100%' height='475px' padding-bottom='56.25%'>").attr("src", "https://www.youtube.com/embed?listType=playlist&list=UUnG-EM6b-Ci0dC0J_GgMxrw")
    iframe.appendTo(get_dom_node(self.latestvidcontainer))
    iframe2 = jQuery("<iframe width='100%' height='475px' padding-bottom='56.25%'>").attr("src", "https://www.youtube.com/embed?listType=playlist&list=UUnG-EM6b-Ci0dC0J_GgMxrw&index=2")
    iframe2.appendTo(get_dom_node(self.nxtvid1container))
    iframe3 = jQuery("<iframe width='100%' height='475px' padding-bottom='56.25%'>").attr("src", "https://www.youtube.com/embed?listType=playlist&list=UUnG-EM6b-Ci0dC0J_GgMxrw&index=3")
    iframe3.appendTo(get_dom_node(self.nxtvid2container))
    iframe4 = jQuery("<iframe width='100%' height='475px' padding-bottom='56.25%'>").attr("src", "https://www.youtube.com/embed?listType=playlist&list=UUnG-EM6b-Ci0dC0J_GgMxrw&index=4")
    iframe4.appendTo(get_dom_node(self.nxtvid3container))
    # Any code you write here will run before the form opens.


