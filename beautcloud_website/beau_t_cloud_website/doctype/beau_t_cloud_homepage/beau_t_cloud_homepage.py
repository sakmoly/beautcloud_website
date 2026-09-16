from frappe.model.document import Document
from frappe.website.utils import clear_cache


class BeauTCloudHomepage(Document):
	def on_update(self):
		clear_cache()
