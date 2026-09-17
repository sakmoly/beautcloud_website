import frappe

from beautcloud_website.website.cms import seed_cms
from beautcloud_website.website.settings import DEFAULTS, IMAGE_SLOTS


def after_install():
	_seed_settings()
	seed_cms()
	_configure_website()
	_ensure_workspace_link()
	_ensure_desk_sidebar()


def after_migrate():
	_seed_settings()
	seed_cms()
	_configure_website()
	_ensure_workspace_link()
	_ensure_desk_sidebar()


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
	if frappe.db.exists("DocType", "Beau-T-Cloud Website Image"):
		existing = {row.slot for row in (doc.get("website_images") or [])}
		for row in IMAGE_SLOTS:
			if row["slot"] not in existing:
				doc.append(
					"website_images",
					{"slot": row["slot"], "label": row["label"], "image": row["image"]},
				)
				changed = True
	if frappe.db.exists("DocType", "Beau-T-Cloud WhatsApp Number") and not doc.get("whatsapp_numbers"):
		india = "".join(ch for ch in str(doc.get("whatsapp_number") or DEFAULTS["whatsapp_number"]) if ch.isdigit())
		saudi = "".join(ch for ch in str(doc.get("whatsapp_number_sa") or "") if ch.isdigit())
		if india:
			doc.append(
				"whatsapp_numbers",
				{
					"country": "India",
					"country_code": "IN",
					"number": india,
					"display": doc.get("whatsapp_display") or DEFAULTS["whatsapp_display"],
					"is_default": 0 if saudi else 1,
				},
			)
		if saudi:
			doc.append(
				"whatsapp_numbers",
				{
					"country": "Saudi Arabia",
					"country_code": "SA",
					"number": saudi,
					"display": doc.get("whatsapp_display_sa") or f"+{saudi}",
					"is_default": 1,
				},
			)
		changed = True
	if changed:
		doc.save(ignore_permissions=True)


def _ensure_workspace_link():
	if not frappe.db.exists("DocType", "Workspace"):
		return
	_ensure_beau_workspace_links()
	if frappe.db.exists("Workspace", "Website"):
		ws = frappe.get_doc("Workspace", "Website")
		already = any(
			(row.get("link_to") == "Beau-T-Cloud Settings") for row in (ws.links or [])
		)
		if not already:
			ws.append(
				"links",
				{
					"type": "Link",
					"label": "Beau-T-Cloud Settings",
					"link_type": "DocType",
					"link_to": "Beau-T-Cloud Settings",
					"onboard": 1,
					"hidden": 0,
				},
			)
			ws.save(ignore_permissions=True)


def _ensure_desk_sidebar():
	if frappe.db.exists("DocType", "Workspace Sidebar") and not frappe.db.exists(
		"Workspace Sidebar", "Beau-T-Cloud"
	):
		sidebar = frappe.new_doc("Workspace Sidebar")
		sidebar.title = "Beau-T-Cloud"
		sidebar.header_icon = "retail"
		sidebar.app = "beautcloud_website"
		sidebar.standard = 1
		sidebar.module = "Beau-T-Cloud Website"
		sidebar.append(
			"items",
			{"label": "Home", "type": "Link", "link_type": "Workspace", "link_to": "Beau-T-Cloud", "icon": "home"},
		)
		sidebar.append(
			"items",
			{
				"label": "Website Settings",
				"type": "Link",
				"link_type": "DocType",
				"link_to": "Beau-T-Cloud Settings",
				"icon": "settings",
			},
		)
		sidebar.append(
			"items",
			{"label": "Leads", "type": "Link", "link_type": "DocType", "link_to": "Lead", "icon": "users"},
		)
		for item in _cms_sidebar_items():
			sidebar.append("items", item)
		sidebar.insert(ignore_permissions=True)

	if frappe.db.exists("DocType", "Workspace Sidebar") and frappe.db.exists("Workspace Sidebar", "Website"):
		try:
			sitebar = frappe.get_doc("Workspace Sidebar", "Website")
			wanted = [
				{
					"label": "Beau-T-Cloud",
					"type": "Link",
					"link_type": "Workspace",
					"link_to": "Beau-T-Cloud",
					"icon": "retail",
				},
				{
					"label": "Beau-T-Cloud Settings",
					"type": "Link",
					"link_type": "DocType",
					"link_to": "Beau-T-Cloud Settings",
					"icon": "settings",
				},
			]
			changed = False
			existing = {(row.link_type, row.link_to) for row in (sitebar.items or [])}
			for item in wanted:
				if (item["link_type"], item["link_to"]) not in existing:
					sitebar.append("items", item)
					changed = True
			if changed:
				sitebar.save(ignore_permissions=True)
		except Exception:
			frappe.log_error(title="Beau-T-Cloud Website sidebar link")

	if frappe.db.exists("DocType", "Desktop Icon"):
		logo = "/assets/beautcloud_website/images/logo/beau-t-cloud-symbol.png"
		if not frappe.db.exists("Desktop Icon", "Beau-T-Cloud"):
			icon = frappe.new_doc("Desktop Icon")
			icon.label = "Beau-T-Cloud"
			icon.icon_type = "Link"
			icon.link_type = "Workspace Sidebar"
			icon.link_to = "Beau-T-Cloud"
			icon.icon = "retail"
			icon.logo_url = logo
			icon.app = "beautcloud_website"
			icon.standard = 1
			icon.hidden = 0
			icon.idx = 1
			icon.insert(ignore_permissions=True)
		else:
			frappe.db.set_value(
				"Desktop Icon",
				"Beau-T-Cloud",
				{
					"hidden": 0,
					"parent_icon": None,
					"icon_type": "Link",
					"link_type": "Workspace Sidebar",
					"link_to": "Beau-T-Cloud",
					"logo_url": logo,
					"app": "beautcloud_website",
					"standard": 1,
				},
				update_modified=False,
			)

		# Old App-type icon used the same logo/name as Beau-T-Cloud and showed twice.
		if frappe.db.exists("Desktop Icon", "Beau-T-Cloud Website"):
			frappe.db.set_value(
				"Desktop Icon",
				"Beau-T-Cloud Website",
				{"hidden": 1},
				update_modified=False,
			)

	_ensure_cms_sidebar_links()
	_clear_desk_cache()


def _cms_sidebar_items():
	return [
		{"label": "Page Sections", "type": "Link", "link_type": "DocType", "link_to": "Beau-T-Cloud Content Section", "icon": "small-file"},
		{"label": "Homepage Copy", "type": "Link", "link_type": "DocType", "link_to": "Beau-T-Cloud Homepage", "icon": "text"},
		{"label": "Features", "type": "Link", "link_type": "DocType", "link_to": "Beau-T-Cloud Feature", "icon": "list"},
		{"label": "Solutions", "type": "Link", "link_type": "DocType", "link_to": "Beau-T-Cloud Solution", "icon": "organization"},
		{"label": "Website Pages", "type": "Link", "link_type": "DocType", "link_to": "Beau-T-Cloud Website Page", "icon": "small-file"},
	]


def _ensure_beau_workspace_links():
	if not frappe.db.exists("Workspace", "Beau-T-Cloud"):
		return
	if not frappe.db.exists("DocType", "Beau-T-Cloud Homepage"):
		return
	ws = frappe.get_doc("Workspace", "Beau-T-Cloud")
	wanted_links = [
		{"label": "Page Sections", "link_to": "Beau-T-Cloud Content Section"},
		{"label": "Homepage Copy", "link_to": "Beau-T-Cloud Homepage"},
		{"label": "Features", "link_to": "Beau-T-Cloud Feature"},
		{"label": "Solutions", "link_to": "Beau-T-Cloud Solution"},
		{"label": "Website Pages", "link_to": "Beau-T-Cloud Website Page"},
	]
	existing_links = {row.get("link_to") for row in (ws.links or [])}
	changed = False
	for item in wanted_links:
		if item["link_to"] not in existing_links:
			ws.append(
				"links",
				{
					"type": "Link",
					"label": item["label"],
					"link_type": "DocType",
					"link_to": item["link_to"],
					"onboard": 1,
					"hidden": 0,
				},
			)
			changed = True
	wanted_shortcuts = [
		{"label": "Page Sections", "link_to": "Beau-T-Cloud Content Section", "color": "Pink", "doc_view": "List"},
		{"label": "Homepage Copy", "link_to": "Beau-T-Cloud Homepage", "color": "Orange", "doc_view": ""},
		{"label": "Features", "link_to": "Beau-T-Cloud Feature", "color": "Blue", "doc_view": "List"},
		{"label": "Solutions", "link_to": "Beau-T-Cloud Solution", "color": "Green", "doc_view": "List"},
		{"label": "Website Pages", "link_to": "Beau-T-Cloud Website Page", "color": "Cyan", "doc_view": "List"},
	]
	existing_shortcuts = {row.get("link_to") for row in (ws.shortcuts or [])}
	for item in wanted_shortcuts:
		if item["link_to"] not in existing_shortcuts:
			ws.append(
				"shortcuts",
				{
					"type": "DocType",
					"label": item["label"],
					"link_to": item["link_to"],
					"color": item["color"],
					"doc_view": item["doc_view"],
				},
			)
			changed = True
	if changed:
		ws.save(ignore_permissions=True)


def _ensure_cms_sidebar_links():
	if not frappe.db.exists("DocType", "Workspace Sidebar"):
		return
	if not frappe.db.exists("Workspace Sidebar", "Beau-T-Cloud"):
		return
	try:
		sidebar = frappe.get_doc("Workspace Sidebar", "Beau-T-Cloud")
		existing = {(row.link_type, row.link_to) for row in (sidebar.items or [])}
		changed = False
		for item in _cms_sidebar_items():
			if (item["link_type"], item["link_to"]) not in existing:
				sidebar.append("items", item)
				changed = True
		if changed:
			sidebar.save(ignore_permissions=True)
	except Exception:
		frappe.log_error(title="Beau-T-Cloud Website CMS sidebar")


def _clear_desk_cache():
	frappe.clear_cache()
	frappe.cache.delete_key("desktop_icons")
	frappe.cache.delete_key("bootinfo")
	for user in frappe.get_all("User", filters={"enabled": 1}, pluck="name"):
		frappe.cache.hdel("desktop_icons", user)
		frappe.cache.hdel("bootinfo", user)
