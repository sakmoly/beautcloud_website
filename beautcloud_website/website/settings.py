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

IMAGE_SLOTS = [
	{"slot": "home_welcome", "label": "Home · Welcome", "image": f"{ASSET}/home/welcome.png"},
	{"slot": "home_lounge", "label": "Home · Lounge", "image": f"{ASSET}/home/lounge.png"},
	{"slot": "home_retail", "label": "Home · Retail", "image": f"{ASSET}/home/retail.png"},
	{"slot": "home_gcc", "label": "Home · GCC", "image": f"{ASSET}/home/gcc.png"},
	{"slot": "page_features", "label": "Features page", "image": f"{ASSET}/pages/features.png"},
	{"slot": "page_solutions", "label": "Solutions page", "image": f"{ASSET}/pages/solutions.png"},
	{"slot": "page_about", "label": "About page", "image": f"{ASSET}/pages/about.png"},
	{"slot": "page_contact", "label": "Contact page", "image": f"{ASSET}/pages/contact.png"},
	{"slot": "page_book_demo", "label": "Book a Demo page", "image": f"{ASSET}/pages/book-demo.png"},
	{"slot": "page_pricing", "label": "Pricing page", "image": f"{ASSET}/pages/pricing.png"},
	{"slot": "page_product_tour", "label": "Product Tour page", "image": f"{ASSET}/pages/product-tour.png"},
	{"slot": "feature_appointment_management", "label": "Feature · Appointments", "image": f"{ASSET}/features/appointment-management.png"},
	{"slot": "feature_online_booking", "label": "Feature · Online Booking", "image": f"{ASSET}/features/online-booking.png"},
	{"slot": "feature_salon_pos", "label": "Feature · Salon POS", "image": f"{ASSET}/features/salon-pos.png"},
	{"slot": "feature_client_crm", "label": "Feature · Client CRM", "image": f"{ASSET}/features/client-crm.png"},
	{"slot": "feature_staff_management", "label": "Feature · Staff", "image": f"{ASSET}/features/staff-management.png"},
	{"slot": "feature_inventory_management", "label": "Feature · Inventory", "image": f"{ASSET}/features/inventory-management.png"},
	{"slot": "feature_memberships_loyalty", "label": "Feature · Memberships", "image": f"{ASSET}/features/memberships-loyalty.png"},
	{"slot": "feature_multi_location", "label": "Feature · Multi-Location", "image": f"{ASSET}/features/multi-location.png"},
	{"slot": "feature_reports_analytics", "label": "Feature · Reports", "image": f"{ASSET}/features/reports-analytics.png"},
	{"slot": "solution_hair_salon", "label": "Solution · Hair Salon", "image": f"{ASSET}/solutions/hair-salon.png"},
	{"slot": "solution_beauty_salon", "label": "Solution · Beauty Salon", "image": f"{ASSET}/solutions/beauty-salon.png"},
	{"slot": "solution_nail_salon", "label": "Solution · Nail Studio", "image": f"{ASSET}/solutions/nail-salon.png"},
	{"slot": "solution_spa", "label": "Solution · Spa", "image": f"{ASSET}/solutions/spa.png"},
	{"slot": "solution_barbershop", "label": "Solution · Barbershop", "image": f"{ASSET}/solutions/barbershop.png"},
	{"slot": "solution_multi_branch", "label": "Solution · Multi-Branch", "image": f"{ASSET}/solutions/multi-branch.png"},
	{"slot": "solution_hair_salon_detail", "label": "Solution · Hair Salon detail", "image": f"{ASSET}/solutions/hair-salon-detail.png"},
	{"slot": "solution_beauty_salon_detail", "label": "Solution · Beauty Salon detail", "image": f"{ASSET}/solutions/beauty-salon-detail.png"},
	{"slot": "solution_nail_salon_detail", "label": "Solution · Nail Studio detail", "image": f"{ASSET}/solutions/nail-salon-detail.png"},
	{"slot": "solution_spa_detail", "label": "Solution · Spa detail", "image": f"{ASSET}/solutions/spa-detail.png"},
	{"slot": "solution_barbershop_detail", "label": "Solution · Barbershop detail", "image": f"{ASSET}/solutions/barbershop-detail.png"},
	{"slot": "solution_multi_branch_detail", "label": "Solution · Multi-Branch detail", "image": f"{ASSET}/solutions/multi-branch-detail.png"},
]

FEATURE_SLOTS = {
	"appointment-management": "feature_appointment_management",
	"online-booking": "feature_online_booking",
	"salon-pos": "feature_salon_pos",
	"client-crm": "feature_client_crm",
	"staff-management": "feature_staff_management",
	"inventory-management": "feature_inventory_management",
	"memberships-loyalty": "feature_memberships_loyalty",
	"multi-location": "feature_multi_location",
	"reports-analytics": "feature_reports_analytics",
}

SOLUTION_SLOTS = {
	"hair-salon": "solution_hair_salon",
	"beauty-salon": "solution_beauty_salon",
	"nail-salon": "solution_nail_salon",
	"spa": "solution_spa",
	"barbershop": "solution_barbershop",
	"multi-branch": "solution_multi_branch",
}

PAGE_SLOTS = {
	"index": "home_welcome",
	"features": "page_features",
	"solutions": "page_solutions",
	"about": "page_about",
	"contact": "page_contact",
	"book-demo": "page_book_demo",
	"pricing": "page_pricing",
	"product-tour": "page_product_tour",
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
	data["images"] = get_image_map()
	return frappe._dict(data)


def get_image_map():
	images = {row["slot"]: _file_url(row["image"]) for row in IMAGE_SLOTS}
	try:
		if frappe.db and frappe.db.exists("DocType", "Beau-T-Cloud Settings"):
			doc = frappe.get_cached_doc("Beau-T-Cloud Settings")
			for row in doc.get("website_images") or []:
				if row.slot and row.image:
					images[row.slot] = _file_url(row.image)
	except Exception:
		frappe.log_error(title="Beau-T-Cloud website images")
	return images


def image_for(slot, fallback=""):
	return get_image_map().get(slot) or fallback
