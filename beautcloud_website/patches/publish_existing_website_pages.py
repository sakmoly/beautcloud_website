import frappe


def execute():
	if not frappe.db.exists("DocType", "Beau-T-Cloud Website Page"):
		return
	if not frappe.db.has_column("Beau-T-Cloud Website Page", "published"):
		return
	for name in frappe.get_all("Beau-T-Cloud Website Page", pluck="name"):
		frappe.db.set_value("Beau-T-Cloud Website Page", name, "published", 1, update_modified=False)
