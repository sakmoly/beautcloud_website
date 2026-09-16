from frappe.model.document import Document
from frappe.website.utils import clear_cache


class BeauTCloudSolution(Document):
	def on_update(self):
		clear_cache()
