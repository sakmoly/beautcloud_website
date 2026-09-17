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
	"whatsapp_number_sa": "",
	"whatsapp_display_sa": "+966",
	"address_line": "King Fahd Road, Al Olaya",
	"city": "Riyadh",
	"country": "Saudi Arabia",
	"login_url": "",
	"book_url": "https://www.beautcloud.com/book",
	"kiosk_url": "https://www.beautcloud.com/kiosk",
	"facebook_url": "https://www.facebook.com/printechs",
	"twitter_url": "https://twitter.com/printechssaudi",
	"linkedin_url": "https://www.linkedin.com/company/printechs",
	"instagram_url": "https://www.instagram.com/printechssaudiarabia",
	"canonical_host": "https://beautcloud.com",
	"google_site_verification": "cv4mnLGBpKqeRhGiK48Y6UYBQ2xPk2jqKRYTaFM_0_0",
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
	{"slot": "page_product_tour", "label": "Product Tour page", "image": f"{ASSET}/hero/hero-salon.png"},
	{"slot": "tour_booking", "label": "Tour · Online booking", "image": f"{ASSET}/features/online-booking.png"},
	{"slot": "tour_kiosk", "label": "Tour · Kiosk", "image": f"{ASSET}/home/lounge.png"},
	{"slot": "tour_calendar", "label": "Tour · Calendar", "image": f"{ASSET}/features/appointment-management.png"},
	{"slot": "tour_crm", "label": "Tour · Client CRM", "image": f"{ASSET}/features/client-crm.png"},
	{"slot": "tour_pos", "label": "Tour · POS", "image": f"{ASSET}/features/salon-pos.png"},
	{"slot": "tour_multi", "label": "Tour · Group view", "image": f"{ASSET}/features/multi-location.png"},
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

TOUR_SLOTS = {
	"book": "tour_booking",
	"booking": "tour_booking",
	"kiosk": "tour_kiosk",
	"calendar": "tour_calendar",
	"crm": "tour_crm",
	"pos": "tour_pos",
	"multi": "tour_multi",
	"analytics": "feature_reports_analytics",
}

TOUR_SHOTS = {
	"book": "booking_screenshot",
	"booking": "booking_screenshot",
	"calendar": "calendar_screenshot",
	"crm": "crm_screenshot",
	"pos": "pos_screenshot",
	"multi": "hero_screenshot",
	"analytics": "hero_screenshot",
}


def _digits(value):
	return "".join(ch for ch in str(value or "") if ch.isdigit())


def _wa_link(value):
	digits = _digits(value)
	return f"https://wa.me/{digits}" if digits else ""


def _whatsapp_rows(doc=None, data=None):
	rows = []
	if doc:
		for item in doc.get("whatsapp_numbers") or []:
			number = _digits(item.number)
			code = (item.country_code or "").strip().upper()
			if not number or not code:
				continue
			rows.append(
				{
					"country": item.country or code,
					"code": code,
					"number": number,
					"display": item.display or f"+{number}",
					"link": _wa_link(number),
					"default": 1 if item.is_default else 0,
				}
			)
	if rows:
		return rows
	data = data or {}
	india = _digits(data.get("whatsapp_number"))
	saudi = _digits(data.get("whatsapp_number_sa"))
	if india:
		rows.append(
			{
				"country": "India",
				"code": "IN",
				"number": india,
				"display": data.get("whatsapp_display") or f"+{india}",
				"link": _wa_link(india),
				"default": 0 if saudi else 1,
			}
		)
	if saudi:
		rows.append(
			{
				"country": "Saudi Arabia",
				"code": "SA",
				"number": saudi,
				"display": data.get("whatsapp_display_sa") or f"+{saudi}",
				"link": _wa_link(saudi),
				"default": 1,
			}
		)
	return rows


def _pick_whatsapp(rows, country=""):
	if not rows:
		return {}
	code = (country or "").upper()
	for row in rows:
		if row["code"] == code:
			return row
	for row in rows:
		if row.get("default"):
			return row
	return rows[0]


def _visitor_country():
	request = getattr(frappe.local, "request", None)
	if not request:
		return ""
	headers = request.headers
	for key in (
		"CF-IPCountry",
		"X-Country-Code",
		"CloudFront-Viewer-Country",
		"X-Appengine-Country",
		"X-Vercel-IP-Country",
	):
		value = (headers.get(key) or "").strip().upper()
		if value and value not in ("XX", "T1", "ZZ"):
			return value
	langs = (headers.get("Accept-Language") or "").lower()
	if "en-in" in langs or "hi-in" in langs or langs.startswith("hi"):
		return "IN"
	return ""


def _file_url(value):
	if not value:
		return ""
	if value.startswith("http") or value.startswith("/"):
		return value
	return frappe.utils.get_url(value)


def get_brand_settings():
	data = dict(DEFAULTS)
	doc = None
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

	rows = _whatsapp_rows(doc, data)
	chosen = _pick_whatsapp(rows, _visitor_country())
	india = next((row for row in rows if row["code"] == "IN"), {})
	saudi = next((row for row in rows if row["code"] == "SA"), {})
	data["whatsapp_numbers"] = rows
	data["whatsapp_numbers_json"] = frappe.as_json(rows)
	data["whatsapp_link"] = chosen.get("link") or ""
	data["whatsapp_display_active"] = chosen.get("display") or ""
	data["whatsapp_country"] = chosen.get("code") or ""
	data["whatsapp_link_in"] = india.get("link") or chosen.get("link") or ""
	data["whatsapp_link_sa"] = saudi.get("link") or chosen.get("link") or ""
	data["whatsapp_display_in"] = india.get("display") or data.get("whatsapp_display") or ""
	phone = "".join(ch for ch in str(data.get("contact_phone") or "") if ch.isdigit())
	placeholder_phones = {"966110000000", "110000000"}
	data["phone_link"] = f"tel:+{phone}" if phone else ""
	data["show_phone"] = bool(phone) and phone not in placeholder_phones
	data["email_link"] = f"mailto:{data['contact_email']}" if data.get("contact_email") else ""
	data["login_url"] = data.get("login_url") or "/book-demo"
	data["social_links"] = social_links_from(data)
	data["images"] = get_image_map()
	return frappe._dict(data)


def social_links_from(data):
	return [
		item
		for item in (
			{"name": "Facebook", "key": "facebook", "url": data.get("facebook_url")},
			{"name": "X", "key": "twitter", "url": data.get("twitter_url")},
			{"name": "LinkedIn", "key": "linkedin", "url": data.get("linkedin_url")},
			{"name": "Instagram", "key": "instagram", "url": data.get("instagram_url")},
		)
		if item.get("url")
	]


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
