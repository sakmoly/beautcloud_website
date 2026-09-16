import frappe

from beautcloud_website.website.cms import (
	business_type_blocks,
	get_feature,
	get_homepage,
	get_nav,
	get_page,
	get_solution,
	home_feature_blocks,
	home_more_blocks,
	list_features,
	list_solutions,
)
from beautcloud_website.website.content import FEATURES, PAGE_IMAGES, PAGES, SOLUTIONS
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


def _apply_feature_image(bc, item):
	item["image"] = _img(bc, FEATURE_SLOTS.get(item.get("slug")), item.get("image"))
	return item


def _apply_solution_image(bc, item):
	item["image"] = _img(bc, SOLUTION_SLOTS.get(item.get("slug")), item.get("image"))
	item["detail_image"] = _img(
		bc, f"{SOLUTION_SLOTS.get(item.get('slug'))}_detail", item.get("detail_image")
	)
	return item


def _cta(home, page=None):
	page = page or {}
	return {
		"eyebrow": page.get("cta_eyebrow") or home.get("cta_eyebrow") or "Next step",
		"title": page.get("cta_title") or home.get("cta_title"),
		"text": page.get("cta_text") or home.get("cta_text"),
		"primary_label": page.get("cta_primary_label") or home.get("cta_primary_label") or "Book a Demo",
		"secondary_label": page.get("cta_secondary_label") or home.get("cta_secondary_label") or "Contact Us",
		"primary_route": page.get("cta_primary_route") or "/book-demo",
		"secondary_route": page.get("cta_secondary_route") or "/contact",
	}


def update_website_context(context):
	bc = get_brand_settings()
	home = get_homepage()
	context.bc = bc
	context.home = home
	context.bc_nav = get_nav()
	context.cta = _cta(home)
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
	context.business_types = [
		{
			**item,
			"image": _img(
				bc,
				SOLUTION_SLOTS.get(item.get("slug") or item["route"].rsplit("/", 1)[-1]),
				item.get("image"),
			),
		}
		for item in business_type_blocks()
	]

	if path in ("", "index"):
		_seo(context, bc, "", home.get("seo_title") or PAGES["index"]["title"], home.get("seo_description") or PAGES["index"]["description"])
		context.page_kind = "home"
		context.faqs = home.get("faq_items") or []
		context.journey = home.get("journey_items") or []
		context.home_features = [
			{
				**item,
				"image": _img(bc, FEATURE_SLOTS.get(item.get("slug") or item["route"].rsplit("/", 1)[-1]), item.get("image")),
				"cta": item.get("cta")
				or f"{home.get('feature_cta_prefix') or 'View'} {item.get('eyebrow')}",
			}
			for item in home_feature_blocks()
		]
		context.home_more = [
			{
				**item,
				"image": _img(bc, FEATURE_SLOTS.get(item.get("slug") or item["route"].rsplit("/", 1)[-1]), item.get("image")),
			}
			for item in home_more_blocks()
		]
		context.home_welcome = _img(bc, "home_welcome", "/assets/beautcloud_website/images/home/welcome.png")
		context.home_lounge = _img(bc, "home_lounge", "/assets/beautcloud_website/images/home/lounge.png")
		context.home_retail = _img(bc, "home_retail", "/assets/beautcloud_website/images/home/retail.png")
		context.home_gcc = _img(bc, "home_gcc", "/assets/beautcloud_website/images/home/gcc.png")
		context.gcc_points = home.get("gcc_items") or []
		context.steps = home.get("step_items") or []
		return context

	if path == "features":
		page = get_page("features")
		_seo(context, bc, path, page.get("seo_title"), page.get("seo_description"))
		context.page_kind = "features_index"
		context.site_page = page
		context.cta = _cta(home, page)
		context.page_image = _img(bc, "page_features", PAGE_IMAGES["features"])
		context.feature_list = [_apply_feature_image(bc, item) for item in list_features()]
		return context

	if path.startswith("features/"):
		slug = path.split("/", 1)[1]
		if slug not in FEATURES and not frappe.db.exists("Beau-T-Cloud Feature", slug):
			return context
		feature = _apply_feature_image(bc, get_feature(slug))
		_seo(context, bc, path, feature.get("seo_title") or feature.get("title"), feature.get("seo_description"), feature.get("image"))
		context.page_kind = "feature"
		context.feature = feature
		context.feature_slug = slug
		context.related_features = [
			_apply_feature_image(bc, get_feature(key))
			for key in feature.get("related", [])
			if key in FEATURES or frappe.db.exists("Beau-T-Cloud Feature", key)
		]
		return context

	if path == "solutions":
		page = get_page("solutions")
		_seo(context, bc, path, page.get("seo_title"), page.get("seo_description"))
		context.page_kind = "solutions_index"
		context.site_page = page
		context.cta = _cta(home, page)
		context.page_image = _img(bc, "page_solutions", PAGE_IMAGES["solutions"])
		context.solution_list = [_apply_solution_image(bc, item) for item in list_solutions()]
		return context

	if path.startswith("solutions/"):
		slug = path.split("/", 1)[1]
		if slug not in SOLUTIONS and not frappe.db.exists("Beau-T-Cloud Solution", slug):
			return context
		solution = _apply_solution_image(bc, get_solution(slug))
		_seo(context, bc, path, solution.get("seo_title") or solution.get("title"), solution.get("seo_description"), solution.get("image"))
		context.page_kind = "solution"
		context.solution = solution
		context.solution_slug = slug
		context.solution_modules = [
			_apply_feature_image(bc, get_feature(key))
			for key in solution.get("modules", [])
			if key in FEATURES or frappe.db.exists("Beau-T-Cloud Feature", key)
		]
		return context

	page = get_page(path) if path in PAGES or frappe.db.exists("Beau-T-Cloud Website Page", path) else None
	if page:
		page_image = _img(bc, PAGE_SLOTS.get(path), PAGE_IMAGES.get(path) or bc.hero_image)
		_seo(
			context,
			bc,
			path,
			page.get("seo_title") or page.get("title"),
			page.get("seo_description"),
			page_image,
		)
		context.page_kind = path.replace("-", "_")
		context.page_image = page_image
		context.site_page = page
		context.cta = _cta(home, page)
		if path == "pricing":
			context.pricing = page.get("pricing") or []
		if path == "product-tour":
			context.tour = page.get("tour") or []
		if path == "about":
			context.about_image = _img(bc, "page_about", PAGE_IMAGES.get("about") or bc.about_image)
	return context
