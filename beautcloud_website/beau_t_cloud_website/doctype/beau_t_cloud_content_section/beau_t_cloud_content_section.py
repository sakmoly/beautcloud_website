import frappe
from frappe.model.document import Document
from frappe.website.utils import clear_cache


class BeauTCloudContentSection(Document):
	def on_update(self):
		clear_cache()

	def after_insert(self):
		clear_cache()
		self._add_to_homepage_layout()

	def on_trash(self):
		clear_cache()

	def _add_to_homepage_layout(self):
		if self.page != "Homepage":
			return
		try:
			if not frappe.db.exists("DocType", "Beau-T-Cloud Homepage"):
				return
			home = frappe.get_single("Beau-T-Cloud Homepage")
			if not home.meta.get_field("page_layout"):
				return
			already = any((row.get("content_section") == self.name) for row in (home.page_layout or []))
			if already:
				return
			home.append(
				"page_layout",
				{
					"section": "Custom section",
					"content_section": self.name,
					"sort_order": self.sort_order or 20,
				},
			)
			home.save(ignore_permissions=True)
		except Exception:
			frappe.log_error(title="Beau-T-Cloud add section to layout")
