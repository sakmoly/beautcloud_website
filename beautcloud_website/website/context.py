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
from beautcloud_website.website.settings import (
	FEATURE_SLOTS,
	PAGE_SLOTS,
	SOLUTION_SLOTS,
	get_brand_settings,
)

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


def _img(bc, slot, fallback=""):
	return (bc.images or {}).get(slot) or fallback


def _feature(bc, slug):
	item = dict(FEATURES[slug])
	item["image"] = _img(bc, FEATURE_SLOTS.get(slug), item.get("image"))
	item["slug"] = slug
	return item


def _solution(bc, slug):
	item = dict(SOLUTIONS[slug])
	item["image"] = _img(bc, SOLUTION_SLOTS.get(slug), item.get("image"))
	item["detail_image"] = _img(bc, f"{SOLUTION_SLOTS.get(slug)}_detail", item.get("detail_image"))
	item["slug"] = slug
	return item


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
		context.business_types = [
			{**item, "image": _img(bc, SOLUTION_SLOTS.get(item["route"].rsplit("/", 1)[-1]), item.get("image"))}
			for item in BUSINESS_TYPES
		]
		context.journey = JOURNEY
		context.home_features = [
			{**item, "image": _img(bc, FEATURE_SLOTS.get(item["route"].rsplit("/", 1)[-1]), item.get("image"))}
			for item in HOME_FEATURES
		]
		context.home_more = [
			{**item, "image": _img(bc, FEATURE_SLOTS.get(item["route"].rsplit("/", 1)[-1]), item.get("image"))}
			for item in HOME_MORE
		]
		context.home_welcome = _img(bc, "home_welcome", "/assets/beautcloud_website/images/home/welcome.png")
		context.home_lounge = _img(bc, "home_lounge", "/assets/beautcloud_website/images/home/lounge.png")
		context.home_retail = _img(bc, "home_retail", "/assets/beautcloud_website/images/home/retail.png")
		context.home_gcc = _img(bc, "home_gcc", "/assets/beautcloud_website/images/home/gcc.png")
		context.gcc_points = GCC_POINTS
		context.steps = STEPS
		return context

	if path == "features":
		_seo(context, bc, path, PAGES["features"]["title"], PAGES["features"]["description"])
		context.page_kind = "features_index"
		context.page_image = _img(bc, "page_features", PAGE_IMAGES["features"])
		context.feature_list = [_feature(bc, slug) for slug in FEATURES]
		return context

	if path.startswith("features/"):
		slug = path.split("/", 1)[1]
		if slug not in FEATURES:
			return context
		feature = _feature(bc, slug)
		_seo(context, bc, path, feature["seo_title"], feature["seo_description"], feature.get("image"))
		context.page_kind = "feature"
		context.feature = feature
		context.feature_slug = slug
		context.related_features = [
			_feature(bc, key) for key in feature.get("related", []) if key in FEATURES
		]
		return context

	if path == "solutions":
		_seo(context, bc, path, PAGES["solutions"]["title"], PAGES["solutions"]["description"])
		context.page_kind = "solutions_index"
		context.page_image = _img(bc, "page_solutions", PAGE_IMAGES["solutions"])
		context.solution_list = [_solution(bc, slug) for slug in SOLUTIONS]
		return context

	if path.startswith("solutions/"):
		slug = path.split("/", 1)[1]
		if slug not in SOLUTIONS:
			return context
		solution = _solution(bc, slug)
		_seo(context, bc, path, solution["seo_title"], solution["seo_description"], solution.get("image"))
		context.page_kind = "solution"
		context.solution = solution
		context.solution_slug = slug
		context.solution_modules = [
			_feature(bc, key) for key in solution.get("modules", []) if key in FEATURES
		]
		return context

	page = PAGES.get(path)
	if page:
		page_image = _img(bc, PAGE_SLOTS.get(path), PAGE_IMAGES.get(path) or bc.hero_image)
		_seo(context, bc, path, page["title"], page["description"], page_image)
		context.page_kind = path.replace("-", "_")
		context.page_image = page_image
		if path == "pricing":
			context.pricing = PRICING
		if path == "product-tour":
			context.tour = TOUR
		if path == "about":
			context.about_image = _img(bc, "page_about", PAGE_IMAGES.get("about") or bc.about_image)
	return context
