import os
import re

import frappe

PAGE_DT = "Beau-T-Cloud Website Page"
CMS_ENDPOINT = "cms-page"
SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,80}$")
RESERVED = {
	"about",
	"api",
	"app",
	"assets",
	"book",
	"book-demo",
	"branches",
	"cms-page",
	"contact",
	"desk",
	"email",
	"features",
	"files",
	"index",
	"kiosk",
	"login",
	"me",
	"p",
	"pricing",
	"print",
	"privacy-policy",
	"private",
	"product-tour",
	"robots.txt",
	"rss",
	"services",
	"sitemap.xml",
	"solutions",
	"staff",
	"terms",
	"third_party",
	"website",
}


def published_page_slugs():
	if not frappe.db:
		return set()
	try:
		if not frappe.db.exists("DocType", PAGE_DT):
			return set()
		filters = {}
		if frappe.db.has_column(PAGE_DT, "published"):
			filters = {"published": 1}
		return set(frappe.get_all(PAGE_DT, filters=filters, pluck="name"))
	except Exception:
		return set()


def is_dynamic_published_page(slug):
	slug = (slug or "").strip("/")
	if not slug or "/" in slug or not SLUG_RE.match(slug) or slug in RESERVED:
		return False
	if _has_www_page(slug):
		return False
	if not frappe.db or not frappe.db.exists("DocType", PAGE_DT):
		return False
	if not frappe.db.exists(PAGE_DT, slug):
		return False
	if frappe.db.has_column(PAGE_DT, "published"):
		return bool(frappe.db.get_value(PAGE_DT, slug, "published"))
	return True


def resolve_website_path(path):
	slug = (path or "").strip("/")
	if is_dynamic_published_page(slug):
		frappe.local.path = slug
		return CMS_ENDPOINT
	from frappe.website.path_resolver import resolve_path

	return resolve_path(path)


def _has_www_page(slug):
	for app in frappe.get_installed_apps():
		www = frappe.get_app_path(app, "www")
		if os.path.exists(os.path.join(www, f"{slug}.html")):
			return True
		if os.path.exists(os.path.join(www, slug, "index.html")):
			return True
	return False
