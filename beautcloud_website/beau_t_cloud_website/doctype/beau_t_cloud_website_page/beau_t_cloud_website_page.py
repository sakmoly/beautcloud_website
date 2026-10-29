import frappe
from frappe.model.document import Document
from frappe.website.utils import clear_cache


class BeauTCloudWebsitePage(Document):
	def on_update(self):
		clear_cache()
		frappe.cache.delete_key("website_404")
