import urllib.error
import urllib.request

import frappe
from werkzeug.exceptions import HTTPException
from werkzeug.wrappers import Response

PRODUCT_HOST = "http://127.0.0.1:3086"
SKIP_REQ = {
	"connection",
	"keep-alive",
	"proxy-authenticate",
	"proxy-authorization",
	"te",
	"trailers",
	"transfer-encoding",
	"upgrade",
	"host",
	"content-length",
}
SKIP_RES = SKIP_REQ | {"content-encoding"}


KIOSK_HOSTS = {"kiosk.beautcloud.com", "kiosk.beautycloud.com"}
KIOSK_REDIRECT = "https://www.beautcloud.com/kiosk"
BOOK_HOSTS = {"book.beautcloud.com", "book.beautycloud.com"}
BOOK_REDIRECT = "https://www.beautcloud.com/book"
POS_HOSTS = {"pos.beautcloud.com", "pos.beautycloud.com"}
POS_REDIRECT = "https://www.beautcloud.com/staff/pos"


def request_host(request) -> str:
	return (request.host or "").split(":")[0].lower()


def should_proxy(path: str) -> bool:
	return (
		path == "/book"
		or path.startswith("/book/")
		or path == "/kiosk"
		or path.startswith("/kiosk/")
		or path == "/staff"
		or path.startswith("/staff/")
		or path == "/services"
		or path.startswith("/services/")
		or path == "/branches"
		or path.startswith("/branches/")
		or path.startswith("/p/")
		or path.startswith("/_next/")
		or path == "/api/beauty"
		or path.startswith("/api/beauty/")
		or path
		in {
			"/favicon.png",
			"/favicon.ico",
			"/icon.png",
			"/apple-icon.png",
			"/apple-touch-icon.png",
			"/beauty-cloud-logo.png",
			"/beauty-cloud-wordmark.png",
			"/manifest.webmanifest",
		}
	)


class ProxiedResponse(HTTPException):
	def __init__(self, response: Response):
		super().__init__()
		self.response = response
		self.code = response.status_code

	def get_response(self, environ=None):
		return self.response


GOOGLE_VERIFY_PATHS = {
	"/googleefbb3bdf2b4aee65e6",
	"/googleefbb3bdf2b4aee65e6.html",
}
GOOGLE_VERIFY_BODY = "google-site-verification: googleefbb3bdf2b4aee65e6.html"


def before_request():
	request = getattr(frappe.local, "request", None)
	if not request:
		return
	if request.path.rstrip("/") in GOOGLE_VERIFY_PATHS:
		raise ProxiedResponse(
			Response(GOOGLE_VERIFY_BODY, status=200, content_type="text/html; charset=utf-8")
		)
	if request_host(request) in KIOSK_HOSTS:
		raise ProxiedResponse(Response(status=301, headers={"Location": KIOSK_REDIRECT}))
	if request_host(request) in BOOK_HOSTS:
		raise ProxiedResponse(Response(status=301, headers={"Location": BOOK_REDIRECT}))
	if request_host(request) in POS_HOSTS:
		raise ProxiedResponse(Response(status=301, headers={"Location": POS_REDIRECT}))
	if request.path in ("/favicon.ico", "/favicon.png"):
		raise ProxiedResponse(
			Response(
				status=302,
				headers={"Location": "/assets/beauty_cloud/images/beauty-cloud-favicon.png"},
			)
		)
	if not should_proxy(request.path):
		return
	raise ProxiedResponse(_fetch(request))


def _fetch(request, path=None):
	target = path if path else request.path
	query = request.query_string.decode() if request.query_string else ""
	url = f"{PRODUCT_HOST}{target}"
	if query:
		url = f"{url}?{query}"
	data = request.get_data() if request.method in ("POST", "PUT", "PATCH", "DELETE") else None
	headers = {
		key: value
		for key, value in request.headers.items()
		if key.lower() not in SKIP_REQ and value
	}
	headers["Host"] = "127.0.0.1:3086"
	headers["X-Forwarded-Host"] = request.host
	headers["X-Forwarded-Proto"] = request.scheme or "https"
	try:
		upstream = urllib.request.Request(url, data=data, headers=headers, method=request.method)
		with urllib.request.urlopen(upstream, timeout=60) as resp:
			return _to_response(resp.status, resp.headers, resp.read())
	except urllib.error.HTTPError as err:
		return _to_response(err.code, err.headers, err.read())
	except Exception:
		return Response(
			"The booking and kiosk app is starting. Refresh in a moment.",
			status=502,
			content_type="text/plain; charset=utf-8",
		)


def _to_response(status, headers, body):
	response = Response(body, status=status)
	for key, value in headers.items():
		if key.lower() in SKIP_RES:
			continue
		if key.lower() == "set-cookie":
			response.headers.add(key, value)
		else:
			response.headers[key] = value
	return response
