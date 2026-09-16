import frappe

from beautcloud_website.website.settings import DEFAULTS


def after_install():
	_seed_settings()
	_configure_website()


def after_migrate():
	_seed_settings()
	_configure_website()


def _configure_website():
	if not frappe.db.exists("DocType", "Website Settings"):
		return
	values = {
		"home_page": "index",
		"app_name": "Beau-T-Cloud",
		"disable_signup": 1,
		"title_prefix": "",
		"favicon": "/assets/beautcloud_website/images/logo/favicon.png",
		"splash_image": "/assets/beautcloud_website/images/logo/beau-t-cloud-symbol.png",
		"banner_image": "/assets/beautcloud_website/images/logo/beau-t-cloud-primary.png",
	}
	for field, value in values.items():
		try:
			frappe.db.set_single_value("Website Settings", field, value)
		except Exception:
			pass


def _seed_settings():
	if not frappe.db.exists("DocType", "Beau-T-Cloud Settings"):
		return
	doc = frappe.get_single("Beau-T-Cloud Settings")
	changed = False
	for field, value in DEFAULTS.items():
		if field.endswith("_screenshot"):
			continue
		if not doc.get(field):
			doc.set(field, value)
			changed = True
	if changed:
		doc.save(ignore_permissions=True)
