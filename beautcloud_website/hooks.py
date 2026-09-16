app_name = "beautcloud_website"
app_title = "Beau-T-Cloud Website"
app_publisher = "Beau-T-Cloud"
app_description = "Official Beau-T-Cloud salon and beauty business management website"
app_email = "mehrin@beautcloud.com"
app_license = "mit"

required_apps = []

home_page = "index"

web_include_css = ["/assets/beautcloud_website/css/beautcloud.css?v=20260916l"]
web_include_js = ["/assets/beautcloud_website/js/beautcloud.js?v=20260916n"]

update_website_context = ["beautcloud_website.website.context.update_website_context"]

base_template_map = {
	r"^/?$": "beautcloud_website/templates/layouts/beautcloud.html",
	r"^index$": "beautcloud_website/templates/layouts/beautcloud.html",
	r"^/?(features|solutions|product-tour|pricing|about|contact|book-demo|privacy-policy|terms)(/.*)?$": (
		"beautcloud_website/templates/layouts/beautcloud.html"
	),
}

after_install = "beautcloud_website.install.after_install"
after_migrate = "beautcloud_website.install.after_migrate"

add_to_apps_screen = [
	{
		"name": "beautcloud_website",
		"logo": "/assets/beautcloud_website/images/logo/beau-t-cloud-symbol.png",
		"title": "Beau-T-Cloud Website",
		"route": "/app/beau-t-cloud",
	}
]

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "beautcloud_website",
# 		"logo": "/assets/beautcloud_website/logo.png",
# 		"title": "Beau-T-Cloud Website",
# 		"route": "/beautcloud_website",
# 		"has_permission": "beautcloud_website.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/beautcloud_website/css/beautcloud_website.css"
# app_include_js = "/assets/beautcloud_website/js/beautcloud_website.js"

# include js, css files in header of web template
# web_include_css = "/assets/beautcloud_website/css/beautcloud_website.css"
# web_include_js = "/assets/beautcloud_website/js/beautcloud_website.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "beautcloud_website/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "beautcloud_website/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "beautcloud_website.utils.jinja_methods",
# 	"filters": "beautcloud_website.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "beautcloud_website.install.before_install"
# after_install = "beautcloud_website.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "beautcloud_website.uninstall.before_uninstall"
# after_uninstall = "beautcloud_website.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "beautcloud_website.utils.before_app_install"
# after_app_install = "beautcloud_website.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "beautcloud_website.utils.before_app_uninstall"
# after_app_uninstall = "beautcloud_website.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "beautcloud_website.build.after_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "beautcloud_website.notifications.get_notification_config"

# Awesome Bar
# -----------
# Extra search results: list of dicts with label, description, route, index.
# route: ["List", "ToDo"], "/desk/docs/some/page", or "https://example.com"
# awesomebar_search = ["beautcloud_website.search.awesomebar_results"]

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"beautcloud_website.tasks.all"
# 	],
# 	"daily": [
# 		"beautcloud_website.tasks.daily"
# 	],
# 	"hourly": [
# 		"beautcloud_website.tasks.hourly"
# 	],
# 	"weekly": [
# 		"beautcloud_website.tasks.weekly"
# 	],
# 	"monthly": [
# 		"beautcloud_website.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "beautcloud_website.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "beautcloud_website.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "beautcloud_website.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "beautcloud_website.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["beautcloud_website.utils.before_request"]
# after_request = ["beautcloud_website.utils.after_request"]

# Job Events
# ----------
# before_job = ["beautcloud_website.utils.before_job"]
# after_job = ["beautcloud_website.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"beautcloud_website.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

