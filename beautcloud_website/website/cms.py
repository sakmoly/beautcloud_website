import frappe

from beautcloud_website.website.content import (
	BUSINESS_TYPES,
	FAQS,
	FEATURES,
	GCC_POINTS,
	HOME_FEATURES,
	HOME_MORE,
	JOURNEY,
	NAV,
	PAGES,
	PRICING,
	SOLUTIONS,
	STEPS,
	TOUR,
)

FEATURE_DT = "Beau-T-Cloud Feature"
SOLUTION_DT = "Beau-T-Cloud Solution"
PAGE_DT = "Beau-T-Cloud Website Page"
HOME_DT = "Beau-T-Cloud Homepage"
ASSET = "/assets/beautcloud_website/images"

HOME_DEFAULTS = {
	"seo_title": PAGES["index"]["title"],
	"seo_description": PAGES["index"]["description"],
	"hero_eyebrow": "The operating system for modern beauty businesses",
	"hero_title": "Run your beauty business beautifully.",
	"hero_lead": "Appointments, clients, staff, POS, inventory, memberships and multiple locations — one connected cloud platform.",
	"hero_primary_label": "Book a Demo",
	"hero_primary_route": "/book-demo",
	"hero_secondary_label": "Explore the Platform",
	"hero_secondary_route": "/product-tour",
	"live_eyebrow": "See it on the floor",
	"live_title": "Open a live booking page. Then walk the rest of the day.",
	"live_text": "The booking and kiosk links open a real salon setup. We do not invent customer counts or fill this page with the same calendar twice.",
	"live_primary_label": "Open live booking",
	"live_secondary_label": "Open kiosk",
	"feature_cta_prefix": "View",
	"more_cta_label": "View feature",
	"types_eyebrow": "Business types",
	"types_title": "Built for every kind of beauty business",
	"types_text": "Whether you run one studio or a group, Beau-T-Cloud follows the way beauty businesses actually work.",
	"journey_eyebrow": "Connected journey",
	"journey_title": "One cloud. Every part of the visit.",
	"journey_text": "Booking, the welcome, the service, payment, rewards and the next visit stay on the same thread.",
	"more_eyebrow": "Also in the platform",
	"more_title": "Booking, loyalty, groups and the day’s numbers.",
	"more_text": "Each tile opens a full page. Figures you see later are examples in SAR, not a customer’s results.",
	"gcc_eyebrow": "Saudi Arabia & GCC",
	"gcc_title": "Implemented for beauty businesses in the region.",
	"gcc_text": "Arabic is prepared as a language switch. Full Arabic copy follows once English is approved. Integrations are named only when they are part of your project.",
	"steps_eyebrow": "Getting started",
	"steps_title": "Three steps. No invented promises.",
	"steps_text": "",
	"faq_eyebrow": "FAQ",
	"faq_title": "Questions, answered plainly.",
	"faq_text": "Legal and security claims stay off this page until they are confirmed.",
	"cta_eyebrow": "Next step",
	"cta_title": "Ready to run the floor from one cloud?",
	"cta_text": "Tell us about your salon, spa or group. We will walk through Beau-T-Cloud around the way you already work.",
	"cta_primary_label": "Book a Demo",
	"cta_secondary_label": "Contact Us",
	"nav_product_label": "Product",
	"nav_solutions_label": "Solutions",
	"nav_pricing_label": "Pricing",
	"nav_pricing_route": "/pricing",
	"nav_resources_label": "Resources",
	"nav_resources_route": "/product-tour",
	"nav_about_label": "About",
	"nav_about_route": "/about",
	"nav_login_label": "Login",
	"nav_login_route": "/login",
	"nav_demo_label": "Book a Demo",
	"nav_demo_route": "/book-demo",
	"footer_blurb": "A Printechs solution for salons, spas and beauty groups.",
	"footer_product_label": "Product",
	"footer_solutions_label": "Solutions",
	"footer_company_label": "Company",
	"footer_resources_label": "Resources",
	"footer_legal": "Beau-T-Cloud. A Printechs solution.",
	"hero_image": f"{ASSET}/hero/hero-salon.png",
	"live_image": f"{ASSET}/home/welcome.png",
	"lounge_image": f"{ASSET}/home/lounge.png",
	"retail_image": f"{ASSET}/home/retail.png",
	"gcc_image": f"{ASSET}/home/gcc.png",
}

NAV_DEFAULTS = [
	{"label": "Product", "menu_type": "Product dropdown", "route": "", "enabled": 1},
	{"label": "Solutions", "menu_type": "Solutions dropdown", "route": "", "enabled": 1},
	{"label": "Pricing", "menu_type": "Link", "route": "/pricing", "enabled": 1},
	{"label": "Resources", "menu_type": "Link", "route": "/product-tour", "enabled": 1},
	{"label": "About", "menu_type": "Link", "route": "/about", "enabled": 1},
]

HOME_BLOCKS = [
	{
		"section": "Hero",
		"image": f"{ASSET}/hero/hero-salon.png",
		"map": {
			"eyebrow": "hero_eyebrow",
			"title": "hero_title",
			"text": "hero_lead",
			"button_label": "hero_primary_label",
			"button_route": "hero_primary_route",
			"secondary_label": "hero_secondary_label",
			"secondary_route": "hero_secondary_route",
			"image": "hero_image",
		},
	},
	{
		"section": "Live booking",
		"image": f"{ASSET}/home/welcome.png",
		"map": {
			"eyebrow": "live_eyebrow",
			"title": "live_title",
			"text": "live_text",
			"button_label": "live_primary_label",
			"secondary_label": "live_secondary_label",
			"image": "live_image",
		},
	},
	{
		"section": "Business types",
		"map": {"eyebrow": "types_eyebrow", "title": "types_title", "text": "types_text"},
	},
	{"section": "Lounge photo", "image": f"{ASSET}/home/lounge.png", "map": {"image": "lounge_image"}},
	{
		"section": "Journey",
		"map": {"eyebrow": "journey_eyebrow", "title": "journey_title", "text": "journey_text"},
	},
	{
		"section": "More modules",
		"map": {
			"eyebrow": "more_eyebrow",
			"title": "more_title",
			"text": "more_text",
			"button_label": "more_cta_label",
		},
	},
	{"section": "Retail photo", "image": f"{ASSET}/home/retail.png", "map": {"image": "retail_image"}},
	{
		"section": "GCC",
		"map": {"eyebrow": "gcc_eyebrow", "title": "gcc_title", "text": "gcc_text"},
	},
	{"section": "GCC photo", "image": f"{ASSET}/home/gcc.png", "map": {"image": "gcc_image"}},
	{
		"section": "Getting started",
		"map": {"eyebrow": "steps_eyebrow", "title": "steps_title", "text": "steps_text"},
	},
	{
		"section": "FAQ",
		"map": {"eyebrow": "faq_eyebrow", "title": "faq_title", "text": "faq_text"},
	},
	{
		"section": "Footer CTA",
		"map": {
			"eyebrow": "cta_eyebrow",
			"title": "cta_title",
			"text": "cta_text",
			"button_label": "cta_primary_label",
			"secondary_label": "cta_secondary_label",
		},
	},
]

DEFAULT_PAGE_LAYOUT = [
	{"section": "Hero", "sort_order": 1},
	{"section": "Live booking", "sort_order": 2},
	{"section": "Business types", "sort_order": 3},
	{"section": "Lounge photo", "sort_order": 4},
	{"section": "Journey", "sort_order": 5},
	{"section": "Feature blocks", "sort_order": 6},
	{"section": "Retail photo", "sort_order": 7},
	{"section": "More modules", "sort_order": 8},
	{"section": "GCC photo", "sort_order": 9},
	{"section": "GCC", "sort_order": 10},
	{"section": "Getting started", "sort_order": 11},
	{"section": "FAQ", "sort_order": 12},
	{"section": "Footer CTA", "sort_order": 13},
]

PAGE_LABELS = {
	"": "Homepage",
	"index": "Homepage",
	"features": "Features",
	"solutions": "Solutions",
	"about": "About",
	"contact": "Contact",
	"book-demo": "Book a Demo",
	"pricing": "Pricing",
	"product-tour": "Product Tour",
	"privacy-policy": "Privacy Policy",
	"terms": "Terms",
}

SECTION_DT = "Beau-T-Cloud Content Section"

LAYOUT_MAP = {
	"Title + image": "Split",
	"Title + image flipped": "Split flipped",
	"Center text": "Center",
	"Photo": "Photo",
	"Cards": "Cards",
	"FAQ": "FAQ",
}

FOOTER_COMPANY = [
	{"title": "About", "link_route": "/about"},
	{"title": "Contact", "link_route": "/contact"},
	{"title": "Book a Demo", "link_route": "/book-demo"},
	{"title": "Product tour", "link_route": "/product-tour"},
]

FOOTER_RESOURCES = [
	{"title": "FAQs", "link_route": "/#faq"},
	{"title": "Privacy", "link_route": "/privacy-policy"},
	{"title": "Terms", "link_route": "/terms"},
	{"title": "Live booking", "kind": "book"},
]

PAGE_DEFAULTS = {
	"features": {
		"title": "Features",
		"seo_title": PAGES["features"]["title"],
		"seo_description": PAGES["features"]["description"],
		"eyebrow": "Product",
		"hero": "Everything in one cloud platform.",
		"lead": "Each module has its own photograph and page. We describe the work — not invented customer results.",
		"button_label": "View feature",
		"cta_title": HOME_DEFAULTS["cta_title"],
		"cta_text": HOME_DEFAULTS["cta_text"],
		"cta_primary_label": "Book a Demo",
		"cta_secondary_label": "Contact Us",
	},
	"solutions": {
		"title": "Solutions",
		"seo_title": PAGES["solutions"]["title"],
		"seo_description": PAGES["solutions"]["description"],
		"eyebrow": "Solutions",
		"hero": "Designed around the way you work.",
		"lead": "The platform is the same cloud. Each page explains the workflow for that kind of beauty business.",
		"button_label": "View solution",
		"cta_title": HOME_DEFAULTS["cta_title"],
		"cta_text": HOME_DEFAULTS["cta_text"],
		"cta_primary_label": "Book a Demo",
		"cta_secondary_label": "Contact Us",
	},
	"product-tour": {
		"title": "Product Tour",
		"seo_title": PAGES["product-tour"]["title"],
		"seo_description": PAGES["product-tour"]["description"],
		"eyebrow": "Product tour",
		"hero": "See the platform, then open the live flow.",
		"lead": "Each step is a different part of the floor. Booking and kiosk open a live salon. The other steps use their own photo until you attach a real screenshot.",
		"cta_title": HOME_DEFAULTS["cta_title"],
		"cta_text": HOME_DEFAULTS["cta_text"],
		"cta_primary_label": "Book a Demo",
		"cta_secondary_label": "Contact Us",
	},
	"pricing": {
		"title": "Pricing",
		"seo_title": PAGES["pricing"]["title"],
		"seo_description": PAGES["pricing"]["description"],
		"eyebrow": "Pricing",
		"hero": "Plans for every stage of your beauty business.",
		"lead": "Subscription prices are not published yet. Choose the shape of your business and talk to sales — we will propose a package after the demo.",
		"note": "Price on consultation",
		"cta_title": HOME_DEFAULTS["cta_title"],
		"cta_text": HOME_DEFAULTS["cta_text"],
		"cta_primary_label": "Book a Demo",
		"cta_secondary_label": "Contact Us",
	},
	"about": {
		"title": "About",
		"seo_title": PAGES["about"]["title"],
		"seo_description": PAGES["about"]["description"],
		"eyebrow": "About",
		"hero": "A Printechs product for beauty operations.",
		"lead": "Beau-T-Cloud helps salons, spas and beauty groups run appointments, clients, staff, sales and inventory from one cloud platform.",
		"cta_title": HOME_DEFAULTS["cta_title"],
		"cta_text": HOME_DEFAULTS["cta_text"],
		"cta_primary_label": "Book a Demo",
		"cta_secondary_label": "Contact Us",
	},
	"contact": {
		"title": "Contact",
		"seo_title": PAGES["contact"]["title"],
		"seo_description": PAGES["contact"]["description"],
		"eyebrow": "Contact",
		"hero": "Speak with the Beau-T-Cloud team.",
		"lead": "Use the details below or send a demo request. These values can be updated later from Beau-T-Cloud Settings.",
		"button_label": "Book a Demo",
	},
	"book-demo": {
		"title": "Book a Demo",
		"seo_title": PAGES["book-demo"]["title"],
		"seo_description": PAGES["book-demo"]["description"],
		"eyebrow": "Book a demo",
		"hero": "See Beau-T-Cloud on your floor.",
		"lead": "Tell us about your salon, spa or group. We walk through the product around how you book, sell and pay staff today.",
		"note": "Required: full name, business name, and either a mobile or email.",
		"aside_title": "What happens next",
		"cta_title": "Prefer to talk now?",
		"button_label": "Request a demo",
	},
	"privacy-policy": {
		"title": "Privacy Policy",
		"seo_title": PAGES["privacy-policy"]["title"],
		"seo_description": PAGES["privacy-policy"]["description"],
		"eyebrow": "Legal",
		"hero": "Privacy policy",
		"lead": "Draft placeholder. Replace this text with the approved policy before production launch.",
		"intro": "<p>Beau-T-Cloud is a Printechs product. This website collects demo and contact requests that you submit. Those requests are stored as leads or communications so the team can reply.</p><p>We do not publish customer lists or tracking claims on this draft page. A complete policy — including cookies, retention and regional rules — will replace these paragraphs.</p><p>To update this page later, change the text on this document in the desk.</p>",
	},
	"terms": {
		"title": "Terms",
		"seo_title": PAGES["terms"]["title"],
		"seo_description": PAGES["terms"]["description"],
		"eyebrow": "Legal",
		"hero": "Website terms",
		"lead": "Draft placeholder. Replace this text with approved terms before production launch.",
		"intro": "<p>The Beau-T-Cloud website describes a software product offered by Printechs. A demo request is not a contract and does not create a subscription.</p><p>Live booking and kiosk links may open a sample salon environment. They are provided for product demonstration and can be changed or removed from Beau-T-Cloud Settings.</p><p>These terms will be replaced with a reviewed version covering licences, acceptable use and governing law.</p>",
	},
}

ABOUT_ITEMS = [
	{"title": "Who builds it", "text": "Beau-T-Cloud is a Printechs solution. The same team that implements the software also supports the business after go-live."},
	{"title": "How we write this site", "text": "We do not publish founder stories, customer counts or awards unless they are approved. Contact details and screenshots can be updated from Beau-T-Cloud Settings."},
	{"title": "Where to start", "text": "Book a demo if you want a walkthrough around your floor. Contact us if you already know what you need to ask."},
]

DEMO_NEXT = [
	{"text": "We read how you book, take payment and pay staff today"},
	{"text": "We walk through Beau-T-Cloud on that workflow"},
	{"text": "You get a written proposal after the call — prices are not listed on the site yet"},
]

FEATURE_LABELS = {
	"change_eyebrow": "How the day changes",
	"problem_label": "The operational problem",
	"solution_label": "How Beau-T-Cloud helps",
	"covers_eyebrow": "In the product",
	"covers_title": "What this module covers",
	"related_title": "Related features",
	"primary_cta_label": "Book a Demo",
	"secondary_cta_label": "All features",
	"live_cta_label": "Open live booking",
}

SOLUTION_LABELS = {
	"challenges_title": "Typical challenges",
	"helps_title": "How Beau-T-Cloud helps",
	"workflow_eyebrow": "A typical workflow",
	"product_eyebrow": "Product",
	"primary_cta_label": "Book a Demo",
	"secondary_cta_label": "All solutions",
}


def _exists(doctype, name=None):
	if not frappe.db.exists("DocType", doctype):
		return False
	if name is None:
		return True
	return bool(frappe.db.exists(doctype, name))


def _lines(items):
	return "\n".join([item for item in (items or []) if item])


def _split_lines(value, fallback=None):
	items = [row.strip() for row in (value or "").splitlines() if row.strip()]
	return items or list(fallback or [])


def _csv(value, fallback=None):
	items = [row.strip() for row in (value or "").split(",") if row.strip()]
	return items or list(fallback or [])


def _copy_rows(items):
	rows = []
	for item in items or []:
		if isinstance(item, str):
			rows.append({"title": item, "text": ""})
			continue
		rows.append(
			{
				"title": item.get("title") or item.get("name") or "",
				"text": item.get("text") or item.get("q") or "",
				"kind": str(item.get("kind") or item.get("num") or ""),
				"link_label": item.get("cta") or item.get("link_label") or "",
				"link_route": item.get("route") or item.get("link_route") or "",
			}
		)
	return rows


def _table_items(doc, field):
	rows = []
	for row in doc.get(field) or []:
		rows.append(
			{
				"title": row.get("title") or "",
				"text": row.get("text") or "",
				"kind": row.get("kind") or "",
				"num": row.get("kind") or "",
				"name": row.get("title") or "",
				"cta": row.get("link_label") or "",
				"route": row.get("link_route") or "",
				"link_label": row.get("link_label") or "",
				"link_route": row.get("link_route") or "",
				"q": row.get("question") or row.get("title") or "",
				"a": row.get("answer") or row.get("text") or "",
			}
		)
	return rows


def _faq_rows(items):
	return [{"question": item["q"], "answer": item["a"]} for item in items]


def _slug_from_route(route):
	return (route or "").rstrip("/").rsplit("/", 1)[-1]


def _home_feature(slug):
	for item in HOME_FEATURES:
		if _slug_from_route(item.get("route")) == slug:
			return item
	return None


def _home_more(slug):
	for item in HOME_MORE:
		if _slug_from_route(item.get("route")) == slug:
			return item
	return None


def _business_type(slug):
	for item in BUSINESS_TYPES:
		if _slug_from_route(item.get("route")) == slug:
			return item
	return None


def seed_cms():
	_seed_homepage()
	_seed_features()
	_seed_solutions()
	_seed_pages()


def _seed_homepage():
	if not _exists(HOME_DT):
		return
	doc = frappe.get_single(HOME_DT)
	changed = False
	for field, value in HOME_DEFAULTS.items():
		if value and not doc.get(field):
			doc.set(field, value)
			changed = True
	tables = {
		"journey_items": _copy_rows(JOURNEY),
		"gcc_items": _copy_rows(GCC_POINTS),
		"step_items": _copy_rows(STEPS),
		"faq_items": _faq_rows(FAQS),
		"footer_company": _copy_rows(FOOTER_COMPANY),
		"footer_resources": _copy_rows(FOOTER_RESOURCES),
		"business_type_cards": [
			{
				"section": "Business types",
				"title": item["title"],
				"text": item["text"],
				"image": item.get("image") or "",
				"route": item.get("route") or "",
				"button_label": "Explore",
			}
			for item in BUSINESS_TYPES
		],
	}
	for field, rows in tables.items():
		if not doc.get(field):
			for row in rows:
				doc.append(field, row)
			changed = True
	if _seed_homepage_blocks(doc):
		changed = True
	for row in doc.get("business_type_cards") or []:
		if not row.get("section"):
			row.section = "Business types"
			changed = True
	if not doc.get("page_layout"):
		for row in DEFAULT_PAGE_LAYOUT:
			doc.append("page_layout", row)
		changed = True
	if _exists("Beau-T-Cloud Nav Item") and not doc.get("nav_items"):
		for row in _nav_seed_rows(doc):
			doc.append("nav_items", row)
		changed = True
	if changed:
		doc.save(ignore_permissions=True)


def _seed_homepage_blocks(doc):
	if doc.get("homepage_sections"):
		return False
	for spec in HOME_BLOCKS:
		row = {"section": spec["section"], "enabled": 1, "image": spec.get("image") or ""}
		for source, field in spec.get("map", {}).items():
			if source == "image":
				continue
			row[source] = doc.get(field) or HOME_DEFAULTS.get(field) or ""
		if not row.get("image"):
			row["image"] = spec.get("image") or ""
		doc.append("homepage_sections", row)
	for row in doc.get("extra_sections") or []:
		if row.get("section") and row.get("section") != "Custom":
			continue
		doc.append(
			"homepage_sections",
			{
				"section": "Custom",
				"enabled": row.get("enabled") if row.get("enabled") is not None else 1,
				"eyebrow": row.get("eyebrow"),
				"title": row.get("title"),
				"text": row.get("text"),
				"image": row.get("image"),
				"button_label": row.get("button_label"),
				"button_route": row.get("button_route"),
				"secondary_label": row.get("secondary_label"),
				"secondary_route": row.get("secondary_route"),
				"place_after": row.get("place_after") or "After FAQ",
				"layout": row.get("layout") or "Split",
				"background": row.get("background") or "Default",
				"anchor_id": row.get("anchor_id"),
			},
		)
	return True


def _seed_features():
	if not _exists(FEATURE_DT):
		return
	for index, (slug, data) in enumerate(FEATURES.items(), start=1):
		if _exists(FEATURE_DT, slug):
			continue
		home = _home_feature(slug)
		more = _home_more(slug)
		doc = frappe.get_doc(
			{
				"doctype": FEATURE_DT,
				"slug": slug,
				"title": data["title"],
				"sort_order": index,
				"seo_title": data.get("seo_title"),
				"seo_description": data.get("seo_description"),
				"eyebrow": data.get("eyebrow"),
				"hero": data.get("hero"),
				"section_title": data.get("section_title"),
				"problem": data.get("problem"),
				"solution": data.get("solution"),
				"points": _lines(data.get("points")),
				"benefits": _lines(data.get("benefits")),
				"related": ", ".join(data.get("related") or []),
				"preview": data.get("preview"),
				"show_live": 1 if data.get("show_live") else 0,
				"show_on_home": 1 if home else 0,
				"show_in_more": 1 if more else 0,
				"home_id": (home or {}).get("id") or "",
				"home_eyebrow": (home or {}).get("eyebrow") or data.get("eyebrow"),
				"home_title": (home or {}).get("title") or "",
				"home_text": (home or {}).get("text") or "",
				"home_points": _lines((home or {}).get("points")),
				"listing_title": (more or {}).get("title") or data.get("title"),
				"listing_text": (more or {}).get("text") or data.get("hero"),
				**FEATURE_LABELS,
			}
		)
		doc.insert(ignore_permissions=True)


def _seed_solutions():
	if not _exists(SOLUTION_DT):
		return
	for index, (slug, data) in enumerate(SOLUTIONS.items(), start=1):
		if _exists(SOLUTION_DT, slug):
			continue
		card = _business_type(slug)
		doc = frappe.get_doc(
			{
				"doctype": SOLUTION_DT,
				"slug": slug,
				"title": data["title"],
				"sort_order": index,
				"seo_title": data.get("seo_title"),
				"seo_description": data.get("seo_description"),
				"eyebrow": data.get("section_eyebrow") or data.get("title"),
				"hero": data.get("hero"),
				"lead": data.get("lead"),
				"section_title": data.get("section_title"),
				"workflow_intro": data.get("workflow_intro"),
				"modules_title": data.get("modules_title"),
				"challenges": _lines(data.get("challenges")),
				"helps": _lines(data.get("helps")),
				"modules": ", ".join(data.get("modules") or []),
				"listing_title": (card or {}).get("title") or data.get("title"),
				"listing_text": (card or {}).get("text") or data.get("lead"),
				**SOLUTION_LABELS,
			}
		)
		for row in _copy_rows(data.get("pillars")):
			doc.append("pillars", row)
		for row in _copy_rows(data.get("workflow")):
			doc.append("workflow", row)
		doc.insert(ignore_permissions=True)


def _seed_pages():
	if not _exists(PAGE_DT):
		return
	for slug, data in PAGE_DEFAULTS.items():
		if _exists(PAGE_DT, slug):
			continue
		doc = frappe.get_doc({"doctype": PAGE_DT, "slug": slug, **data})
		if slug == "about":
			for row in ABOUT_ITEMS:
				doc.append("body_items", row)
		elif slug == "book-demo":
			for row in DEMO_NEXT:
				doc.append("body_items", row)
		elif slug == "pricing":
			for row in _copy_rows(PRICING):
				doc.append("body_items", row)
		elif slug == "product-tour":
			for row in _copy_rows(TOUR):
				doc.append("body_items", row)
		doc.insert(ignore_permissions=True)


def _nav_seed_rows(doc=None):
	data = dict(HOME_DEFAULTS)
	if doc:
		for field in (
			"nav_product_label",
			"nav_solutions_label",
			"nav_pricing_label",
			"nav_pricing_route",
			"nav_resources_label",
			"nav_resources_route",
			"nav_about_label",
			"nav_about_route",
		):
			if doc.get(field) not in (None, ""):
				data[field] = doc.get(field)
	return [
		{"label": data["nav_product_label"], "menu_type": "Product dropdown", "route": "", "enabled": 1},
		{"label": data["nav_solutions_label"], "menu_type": "Solutions dropdown", "route": "", "enabled": 1},
		{"label": data["nav_pricing_label"], "menu_type": "Link", "route": data["nav_pricing_route"], "enabled": 1},
		{"label": data["nav_resources_label"], "menu_type": "Link", "route": data["nav_resources_route"], "enabled": 1},
		{"label": data["nav_about_label"], "menu_type": "Link", "route": data["nav_about_route"], "enabled": 1},
	]


def _nav_menu(doc, data):
	rows = []
	if doc:
		for row in doc.get("nav_items") or []:
			if not row.get("label"):
				continue
			rows.append(
				{
					"label": row.get("label"),
					"type": row.get("menu_type") or "Link",
					"route": row.get("route") or "",
					"enabled": 1 if row.get("enabled") else 0,
				}
			)
	if not rows:
		rows = [
			{"label": item["label"], "type": item["menu_type"], "route": item.get("route") or "", "enabled": 1}
			for item in _nav_seed_rows()
		]
	return [item for item in rows if item.get("enabled")]


def get_homepage():
	data = dict(HOME_DEFAULTS)
	data["journey_items"] = list(JOURNEY)
	data["gcc_items"] = list(GCC_POINTS)
	data["step_items"] = list(STEPS)
	data["faq_items"] = list(FAQS)
	data["footer_company"] = _copy_rows(FOOTER_COMPANY)
	data["footer_resources"] = _copy_rows(FOOTER_RESOURCES)
	data["extra_sections"] = []
	data["business_type_cards"] = []
	data["nav_menu"] = _nav_menu(None, data)
	if not _exists(HOME_DT):
		return data
	try:
		doc = frappe.get_cached_doc(HOME_DT)
	except Exception:
		return data
	for field in HOME_DEFAULTS:
		if doc.get(field) not in (None, ""):
			data[field] = doc.get(field)
	if doc.get("journey_items"):
		data["journey_items"] = _table_items(doc, "journey_items")
	if doc.get("gcc_items"):
		data["gcc_items"] = _table_items(doc, "gcc_items")
	if doc.get("step_items"):
		data["step_items"] = _table_items(doc, "step_items")
	if doc.get("faq_items"):
		data["faq_items"] = _table_items(doc, "faq_items")
	if doc.get("footer_company"):
		data["footer_company"] = _table_items(doc, "footer_company")
	if doc.get("footer_resources"):
		data["footer_resources"] = _table_items(doc, "footer_resources")
	data["nav_menu"] = _nav_menu(doc, data)
	data["section_cards"] = _section_card_map(doc)
	data["business_type_cards"] = data["section_cards"].get("Business types", [])
	_apply_homepage_blocks(doc, data, data["section_cards"])
	data["extra_sections"] = list(data.get("extra_sections") or []) + list_content_sections(
		"Homepage", ""
	)
	return data


PLACE_AFTER = {
	"After hero": "hero",
	"After live booking": "live",
	"After business types": "types",
	"After journey": "journey",
	"After feature blocks": "features",
	"After more modules": "more",
	"After GCC": "gcc",
	"After getting started": "steps",
	"After FAQ": "faq",
	"hero": "hero",
	"live": "live",
	"types": "types",
	"journey": "journey",
	"features": "features",
	"more": "more",
	"gcc": "gcc",
	"steps": "steps",
	"faq": "faq",
}


def _section_card_map(doc):
	grouped = {}
	for row in doc.get("business_type_cards") or []:
		if not row.get("title"):
			continue
		key = (row.get("section") or "Business types").strip()
		grouped.setdefault(key, []).append(
			{
				"title": row.get("title") or "",
				"text": row.get("text") or "",
				"image": row.get("image") or "",
				"route": row.get("route") or "",
				"button_label": row.get("button_label") or "Explore",
				"slug": _slug_from_route(row.get("route") or ""),
				"section": key,
			}
		)
	return grouped


def _apply_homepage_blocks(doc, data, card_map=None):
	card_map = card_map if card_map is not None else _section_card_map(doc)
	blocks = doc.get("homepage_sections") or []
	legacy = [row for row in (doc.get("extra_sections") or []) if (row.get("section") or "Custom") == "Custom"]
	data["extra_sections"] = []
	by_name = {spec["section"]: spec for spec in HOME_BLOCKS}
	for row in list(blocks) + list(legacy):
		if row.get("enabled") in (0, "0"):
			continue
		name = (row.get("section") or "Custom").strip()
		if name in by_name and name != "Custom":
			spec = by_name[name]
			for source, field in spec.get("map", {}).items():
				value = row.get(source)
				if value not in (None, ""):
					data[field] = value
			continue
		data["extra_sections"].append(_custom_block(row, card_map.get(name, [])))


def _custom_block(row, cards=None):
	theme = {"Default": "", "Alt": "bc-section-alt", "Blush": "bc-section-blush"}
	cards = cards or []
	layout = row.get("layout") or "Split"
	if cards and layout == "Split":
		layout = "Cards"
	return {
		"eyebrow": row.get("eyebrow") or "",
		"title": row.get("title") or "",
		"text": row.get("text") or "",
		"image": row.get("image") or "",
		"layout": layout,
		"background": row.get("background") or "Default",
		"theme_class": theme.get(row.get("background") or "Default", ""),
		"button_label": row.get("button_label") or "",
		"button_route": row.get("button_route") or "",
		"secondary_label": row.get("secondary_label") or "",
		"secondary_route": row.get("secondary_route") or "",
		"place_after": PLACE_AFTER.get(row.get("place_after") or "After FAQ", "faq"),
		"anchor_id": row.get("anchor_id") or "",
		"cards": cards,
	}


def _extra_sections(doc):
	data = {"extra_sections": []}
	_apply_homepage_blocks(doc, data)
	return data["extra_sections"]


def list_content_sections(page_label, path=""):
	if not _exists(SECTION_DT):
		return []
	filters = {"enabled": 1}
	names = []
	if page_label:
		names.extend(
			frappe.get_all(
				SECTION_DT,
				filters={**filters, "page": page_label},
				pluck="name",
				order_by="sort_order asc, modified desc",
			)
		)
	if path:
		names.extend(
			frappe.get_all(
				SECTION_DT,
				filters={**filters, "page_path": path},
				pluck="name",
				order_by="sort_order asc, modified desc",
			)
		)
	seen = set()
	blocks = []
	for name in names:
		if name in seen:
			continue
		seen.add(name)
		blocks.append(_content_block(frappe.get_cached_doc(SECTION_DT, name)))
	return blocks


def _content_block(doc):
	theme = {"Default": "", "Alt": "bc-section-alt", "Blush": "bc-section-blush"}
	cards = []
	for row in doc.get("cards") or []:
		if not row.get("title"):
			continue
		cards.append(
			{
				"title": row.get("title") or "",
				"text": row.get("text") or "",
				"image": row.get("image") or "",
				"route": row.get("route") or "",
				"button_label": row.get("button_label") or "Explore",
			}
		)
	faqs = []
	for row in doc.get("faq_items") or []:
		if row.get("question"):
			faqs.append({"q": row.get("question"), "a": row.get("answer") or ""})
	return {
		"eyebrow": doc.get("eyebrow") or "",
		"title": doc.get("title") or "",
		"text": doc.get("description") or "",
		"image": doc.get("image") or "",
		"layout": LAYOUT_MAP.get(doc.get("layout") or "Title + image", "Split"),
		"background": doc.get("background") or "Default",
		"theme_class": theme.get(doc.get("background") or "Default", ""),
		"button_label": doc.get("button_label") or "",
		"button_route": doc.get("button_route") or "",
		"secondary_label": doc.get("secondary_label") or "",
		"secondary_route": doc.get("secondary_route") or "",
		"place_after": PLACE_AFTER.get(doc.get("place_after") or "After FAQ", "faq"),
		"anchor_id": "",
		"cards": cards,
		"faq_items": faqs,
	}


def get_feature(slug):
	base = dict(FEATURES.get(slug) or {})
	base["slug"] = slug
	base.update(FEATURE_LABELS)
	if slug in FEATURES:
		base.setdefault("points", list(FEATURES[slug].get("points") or []))
		base.setdefault("benefits", list(FEATURES[slug].get("benefits") or []))
		base.setdefault("related", list(FEATURES[slug].get("related") or []))
	home = _home_feature(slug)
	more = _home_more(slug)
	if home:
		base["show_on_home"] = 1
		base["home_id"] = home.get("id")
		base["home_eyebrow"] = home.get("eyebrow")
		base["home_title"] = home.get("title")
		base["home_text"] = home.get("text")
		base["home_points"] = list(home.get("points") or [])
	if more:
		base["show_in_more"] = 1
		base["listing_title"] = more.get("title")
		base["listing_text"] = more.get("text")
	if not _exists(FEATURE_DT, slug):
		return base
	doc = frappe.get_cached_doc(FEATURE_DT, slug)
	scalars = [
		"title",
		"seo_title",
		"seo_description",
		"eyebrow",
		"hero",
		"section_title",
		"problem",
		"solution",
		"preview",
		"home_id",
		"home_eyebrow",
		"home_title",
		"home_text",
		"listing_title",
		"listing_text",
		"home_cta_label",
		*FEATURE_LABELS,
	]
	for field in scalars:
		if doc.get(field) not in (None, ""):
			base[field] = doc.get(field)
	base["show_live"] = 1 if doc.get("show_live") else base.get("show_live")
	base["show_on_home"] = 1 if doc.get("show_on_home") else 0
	base["show_in_more"] = 1 if doc.get("show_in_more") else 0
	base["sort_order"] = doc.get("sort_order") or 0
	if doc.get("points"):
		base["points"] = _split_lines(doc.points)
	if doc.get("benefits"):
		base["benefits"] = _split_lines(doc.benefits)
	if doc.get("related"):
		base["related"] = _csv(doc.related)
	if doc.get("home_points"):
		base["home_points"] = _split_lines(doc.home_points)
	return base


def get_solution(slug):
	base = dict(SOLUTIONS.get(slug) or {})
	base["slug"] = slug
	base.update(SOLUTION_LABELS)
	base["eyebrow"] = base.get("section_eyebrow") or base.get("title")
	card = _business_type(slug)
	if card:
		base["listing_title"] = card.get("title")
		base["listing_text"] = card.get("text")
	if not _exists(SOLUTION_DT, slug):
		return base
	doc = frappe.get_cached_doc(SOLUTION_DT, slug)
	scalars = [
		"title",
		"seo_title",
		"seo_description",
		"eyebrow",
		"hero",
		"lead",
		"section_title",
		"workflow_intro",
		"modules_title",
		"listing_title",
		"listing_text",
		*SOLUTION_LABELS,
	]
	for field in scalars:
		if doc.get(field) not in (None, ""):
			base[field] = doc.get(field)
	base["sort_order"] = doc.get("sort_order") or 0
	if doc.get("challenges"):
		base["challenges"] = _split_lines(doc.challenges)
	if doc.get("helps"):
		base["helps"] = _split_lines(doc.helps)
	if doc.get("modules"):
		base["modules"] = _csv(doc.modules)
	if doc.get("pillars"):
		base["pillars"] = _table_items(doc, "pillars")
	if doc.get("workflow"):
		base["workflow"] = _table_items(doc, "workflow")
	return base


def get_page(slug):
	data = dict(PAGE_DEFAULTS.get(slug) or {})
	meta = PAGES.get(slug) or {}
	data.setdefault("seo_title", meta.get("title"))
	data.setdefault("seo_description", meta.get("description"))
	data.setdefault("title", meta.get("title") or slug)
	if slug == "about":
		data["body_items"] = list(ABOUT_ITEMS)
	elif slug == "book-demo":
		data["body_items"] = list(DEMO_NEXT)
	elif slug == "pricing":
		data["body_items"] = _copy_rows(PRICING)
		data["pricing"] = list(PRICING)
	elif slug == "product-tour":
		data["body_items"] = _copy_rows(TOUR)
		data["tour"] = list(TOUR)
	if not _exists(PAGE_DT, slug):
		return data
	doc = frappe.get_cached_doc(PAGE_DT, slug)
	for field in (
		"title",
		"seo_title",
		"seo_description",
		"eyebrow",
		"hero",
		"lead",
		"intro",
		"button_label",
		"note",
		"aside_title",
		"cta_title",
		"cta_text",
		"cta_primary_label",
		"cta_secondary_label",
	):
		if doc.get(field) not in (None, ""):
			data[field] = doc.get(field)
	if doc.get("body_items"):
		data["body_items"] = _table_items(doc, "body_items")
	if doc.get("faq_items"):
		data["faq_items"] = _table_items(doc, "faq_items")
	if slug == "pricing":
		data["pricing"] = [
			{
				"name": row.get("title") or row.get("name"),
				"text": row.get("text"),
				"cta": row.get("link_label") or row.get("cta") or "Book a Demo",
				"route": row.get("link_route") or row.get("route") or "/book-demo",
			}
			for row in data.get("body_items") or []
		]
	if slug == "product-tour":
		from beautcloud_website.website.settings import TOUR_SHOTS, TOUR_SLOTS, image_for

		defaults = {item["kind"]: item for item in TOUR}
		data["tour"] = []
		for row in data.get("body_items") or []:
			kind = row.get("kind") or "calendar"
			base = defaults.get(kind) or {}
			shot_field = TOUR_SHOTS.get(kind)
			shot = ""
			if shot_field:
				try:
					shot = frappe.get_cached_doc("Beau-T-Cloud Settings").get(shot_field) or ""
				except Exception:
					shot = ""
			data["tour"].append(
				{
					"title": row.get("title") or base.get("title"),
					"text": row.get("text") or base.get("text"),
					"kind": kind,
					"cta": row.get("link_label") or base.get("cta") or "Learn more",
					"route": row.get("link_route") or base.get("route") or "",
					"image": shot or image_for(TOUR_SLOTS.get(kind) or "page_product_tour"),
				}
			)
		if not data["tour"]:
			data["tour"] = [
				{
					**item,
					"image": image_for(TOUR_SLOTS.get(item["kind"]) or "page_product_tour"),
				}
				for item in TOUR
			]
	return data


def list_features():
	if _exists(FEATURE_DT):
		names = frappe.get_all(FEATURE_DT, pluck="name", order_by="sort_order asc, name asc")
		if names:
			return [get_feature(name) for name in names]
	return [get_feature(slug) for slug in FEATURES]


def list_solutions():
	if _exists(SOLUTION_DT):
		names = frappe.get_all(SOLUTION_DT, pluck="name", order_by="sort_order asc, name asc")
		if names:
			return [get_solution(name) for name in names]
	return [get_solution(slug) for slug in SOLUTIONS]


def get_nav():
	features = list_features()
	solutions = list_solutions()
	if not features and not solutions:
		return NAV
	return {
		"product": [{"label": item["title"], "route": f"/features/{item['slug']}"} for item in features],
		"solutions": [{"label": item["title"], "route": f"/solutions/{item['slug']}"} for item in solutions],
	}


def home_feature_blocks():
	blocks = []
	for item in list_features():
		if not item.get("show_on_home") and not item.get("home_title"):
			continue
		if not item.get("show_on_home"):
			continue
		blocks.append(
			{
				"id": item.get("home_id") or item["slug"],
				"eyebrow": item.get("home_eyebrow") or item.get("eyebrow"),
				"title": item.get("home_title") or item.get("title"),
				"text": item.get("home_text") or item.get("hero"),
				"points": item.get("home_points") or item.get("points") or [],
				"preview": item.get("preview"),
				"route": f"/features/{item['slug']}",
				"cta": item.get("home_cta_label")
				or f"{HOME_DEFAULTS['feature_cta_prefix']} {item.get('home_eyebrow') or item.get('eyebrow') or item.get('title')}",
				"slug": item["slug"],
				"image": item.get("image"),
			}
		)
	return blocks or [
		{
			**item,
			"cta": f"{HOME_DEFAULTS['feature_cta_prefix']} {item.get('eyebrow')}",
			"slug": _slug_from_route(item.get("route")),
		}
		for item in HOME_FEATURES
	]


def home_more_blocks():
	blocks = []
	for item in list_features():
		if not item.get("show_in_more"):
			continue
		blocks.append(
			{
				"title": item.get("listing_title") or item.get("title"),
				"text": item.get("listing_text") or item.get("hero"),
				"route": f"/features/{item['slug']}",
				"slug": item["slug"],
				"image": item.get("image"),
			}
		)
	return blocks or list(HOME_MORE)


def business_type_blocks():
	home = get_homepage()
	if home.get("business_type_cards"):
		return list(home["business_type_cards"])
	blocks = []
	for item in list_solutions():
		blocks.append(
			{
				"title": item.get("listing_title") or item.get("title"),
				"text": item.get("listing_text") or item.get("lead") or item.get("hero"),
				"route": f"/solutions/{item['slug']}",
				"slug": item["slug"],
				"image": item.get("image"),
				"button_label": "Explore",
			}
		)
	return blocks or list(BUSINESS_TYPES)
