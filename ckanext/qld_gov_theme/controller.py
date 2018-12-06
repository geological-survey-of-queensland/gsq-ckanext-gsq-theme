import ckan.plugins as p
from ckan.lib.base import BaseController

class PermitController(BaseController):
	def permit(self):
		return p.toolkit.url_for('/permit')