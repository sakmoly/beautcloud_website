import frappe

ASSET = "/assets/beautcloud_website/images"

DEFAULTS = {
	"brand_name": "Beau-T-Cloud",
	"company_name": "Printechs",
	"tagline": "Run your beauty business beautifully.",
	"supporting_line": "One Cloud. Every Part of Your Beauty Business.",
	"contact_email": "hello@beautcloud.com",
	"contact_phone": "966110000000",
	"contact_phone_display": "+966 11 000 0000",
	"whatsapp_number": "918075216948",
	"whatsapp_display": "+91 80752 16948",
	"address_line": "King Fahd Road, Al Olaya",
	"city": "Riyadh",
	"country": "Saudi Arabia",
	"login_url": "",
	"book_url": "http://printechsdammam.dyndns.org:86/book",
	"kiosk_url": "http://printechsdammam.dyndns.org:86/kiosk",
	"canonical_host": "https://beautcloud.com",
	"logo": f"{ASSET}/logo/beau-t-cloud-primary.png",
	"symbol": f"{ASSET}/logo/beau-t-cloud-symbol.png",
	"favicon": f"{ASSET}/logo/favicon.png",
	"hero_image": f"{ASSET}/hero/hero-salon.png",
	"about_image": f"{ASSET}/hero/about-atelier.png",
	"hero_screenshot": "",
	"calendar_screenshot": "",
	"booking_screenshot": "",
	"crm_screenshot": "",
	"pos_screenshot": "",
}


def _file_url(value):
	if not value:
		return ""
	if value.startswith("http") or value.startswith("/"):
		return value
	return frappe.utils.get_url(value)


def get_brand_settings():
	data = dict(DEFAULTS)
	try:
		if frappe.db and frappe.db.exists("DocType", "Beau-T-Cloud Settings"):
			doc = frappe.get_cached_doc("Beau-T-Cloud Settings")
			for key in DEFAULTS:
				value = doc.get(key)
				if value not in (None, ""):
					data[key] = value
	except Exception:
		frappe.log_error(title="Beau-T-Cloud Settings load")

	for image_key in (
		"logo",
		"symbol",
		"favicon",
		"hero_image",
		"about_image",
		"hero_screenshot",
		"calendar_screenshot",
		"booking_screenshot",
		"crm_screenshot",
		"pos_screenshot",
	):
		data[image_key] = _file_url(data.get(image_key))

	whatsapp = "".join(ch for ch in str(data.get("whatsapp_number") or "") if ch.isdigit())
	data["whatsapp_link"] = f"https://wa.me/{whatsapp}" if whatsapp else ""
	phone = "".join(ch for ch in str(data.get("contact_phone") or "") if ch.isdigit())
	data["phone_link"] = f"tel:+{phone}" if phone else ""
	data["email_link"] = f"mailto:{data['contact_email']}" if data.get("contact_email") else ""
	data["login_url"] = data.get("login_url") or "/book-demo"
	return frappe._dict(data)
