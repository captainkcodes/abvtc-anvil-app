from ._anvil_designer import SocialsTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.users

from anvil.js.window import jQuery
from anvil.js import get_dom_node

class Socials(SocialsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    iframe = jQuery("<iframe width='100%' height='800px' style='border:solid 1px #777' frameborder='0' scrolling='no'>").attr("src", "https://calendar.google.com/calendar/embed?src=real.abovetheclouds%40gmail.com&ctz=America%2FChicago")
    iframe.appendTo(get_dom_node(self.calcontainer))
    # Any code you write here will run before the form opens.
