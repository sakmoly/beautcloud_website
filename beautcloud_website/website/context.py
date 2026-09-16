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
	PAGE_IMAGES,
	PAGES,
	PRICING,
	SOLUTIONS,
	STEPS,
	TOUR,
)
from beautcloud_website.website.settings import get_brand_settings

MARKETING_ROOTS = {
	"",
	"index",
	"features",
	"solutions",
	"product-tour",
	"pricing",
	"about",
	"contact",
	"book-demo",
	"privacy-policy",
	"terms",
}


def _request_path():
	request = getattr(frappe.local, "request", None)
	path = (getattr(request, "path", None) or getattr(frappe.local, "path", "") or "").strip()
	return path.strip("/")


def _canonical(bc, path):
	host = (bc.canonical_host or "https://beautcloud.com").rstrip("/")
	if not path or path == "index":
		return host + "/"
	return f"{host}/{path}"


def _abs_url(bc, url):
	if not url:
		return ""
	if url.startswith("http://") or url.startswith("https://"):
		return url
	host = (bc.canonical_host or "https://beautcloud.com").rstrip("/")
	return host + (url if url.startswith("/") else "/" + url)


def _seo(context, bc, path, title, description, image=None):
	page_title = title
	canonical = _canonical(bc, path)
	og_image = _abs_url(
		bc,
		image or PAGE_IMAGES.get(path or "index") or bc.hero_image or bc.hero_screenshot or bc.logo,
	)
	context.title = page_title
	context.meta_description = description
	context.metatags = {
		"title": page_title,
		"description": description,
		"image": og_image,
		"og:title": page_title,
		"og:description": description,
		"og:image": og_image,
		"og:url": canonical,
		"og:type": "website",
		"og:site_name": bc.brand_name or "Beau-T-Cloud",
		"twitter:card": "summary_large_image",
		"twitter:title": page_title,
		"twitter:description": description,
		"twitter:image": og_image,
	}
	context.canonical = canonical
	context.bc_canonical = canonical


def update_website_context(context):
	bc = get_brand_settings()
	context.bc = bc
	context.bc_nav = NAV
	context.current_year = frappe.utils.nowdate()[:4]
	path = (context.get("path") or context.get("route") or _request_path() or "").strip("/")
	if path == "index":
		path = ""
	root = path.split("/")[0] if path else ""

	if path not in ("", "index") and root not in MARKETING_ROOTS:
		return context

	context.base_template = "beautcloud_website/templates/layouts/beautcloud.html"
	context.body_class = f"{context.get('body_class') or ''} bc-body".strip()
	context.full_width = 1
	context.show_sidebar = 0
	context.no_breadcrumbs = 1
	context.no_cache = 1
	context.favicon = bc.favicon

	if path in ("", "index"):
		_seo(context, bc, "", PAGES["index"]["title"], PAGES["index"]["description"])
		context.page_kind = "home"
		context.faqs = FAQS
		context.business_types = BUSINESS_TYPES
		context.journey = JOURNEY
		context.home_features = HOME_FEATURES
		context.home_more = HOME_MORE
		context.home_welcome = "/assets/beautcloud_website/images/home/welcome.png"
		context.home_lounge = "/assets/beautcloud_website/images/home/lounge.png"
		context.home_retail = "/assets/beautcloud_website/images/home/retail.png"
		context.home_gcc = "/assets/beautcloud_website/images/home/gcc.png"
		context.gcc_points = GCC_POINTS
		context.steps = STEPS
		return context

	if path == "features":
		_seo(context, bc, path, PAGES["features"]["title"], PAGES["features"]["description"])
		context.page_kind = "features_index"
		context.page_image = PAGE_IMAGES["features"]
		context.feature_list = [{"slug": slug, **item} for slug, item in FEATURES.items()]
		return context

	if path.startswith("features/"):
		slug = path.split("/", 1)[1]
		feature = FEATURES.get(slug)
		if not feature:
			return context
		_seo(context, bc, path, feature["seo_title"], feature["seo_description"], feature.get("image"))
		context.page_kind = "feature"
		context.feature = feature
		context.feature_slug = slug
		context.related_features = [FEATURES[key] | {"slug": key} for key in feature.get("related", []) if key in FEATURES]
		return context

	if path == "solutions":
		_seo(context, bc, path, PAGES["solutions"]["title"], PAGES["solutions"]["description"])
		context.page_kind = "solutions_index"
		context.page_image = PAGE_IMAGES["solutions"]
		context.solution_list = [{"slug": slug, **item} for slug, item in SOLUTIONS.items()]
		return context

	if path.startswith("solutions/"):
		slug = path.split("/", 1)[1]
		solution = SOLUTIONS.get(slug)
		if not solution:
			return context
		_seo(context, bc, path, solution["seo_title"], solution["seo_description"], solution.get("image"))
		context.page_kind = "solution"
		context.solution = solution
		context.solution_slug = slug
		context.solution_modules = [
			{"slug": key, **FEATURES[key]} for key in solution.get("modules", []) if key in FEATURES
		]
		return context

	page = PAGES.get(path)
	if page:
		_seo(context, bc, path, page["title"], page["description"])
		context.page_kind = path.replace("-", "_")
		context.page_image = PAGE_IMAGES.get(path) or bc.hero_image
		if path == "pricing":
			context.pricing = PRICING
		if path == "product-tour":
			context.tour = TOUR
		if path == "about":
			context.about_image = PAGE_IMAGES.get("about") or bc.about_image
	return context
