import re
from datetime import datetime

import frappe
from frappe import _
from frappe.rate_limiter import rate_limit
from frappe.utils import escape_html, validate_email_address

PHONE_RE = re.compile(r"^[0-9+\-\s()]{7,20}$")
NAME_RE = re.compile(r"^[A-Za-zÀ-ÿĀ-ž'\-.\s]{2,80}$")


def _clean(value, limit=140):
	return escape_html((value or "").strip())[:limit]


def _split_name(full_name):
	parts = [part for part in full_name.split() if part]
	first = parts[0] if parts else full_name
	last = " ".join(parts[1:]) if len(parts) > 1 else ""
	return first, last


@frappe.whitelist(allow_guest=True)
@rate_limit(limit=8, seconds=60 * 60)
def submit_demo(**kwargs):
	honeypot = _clean(kwargs.get("website") or kwargs.get("company_website"), 80)
	if honeypot:
		return {"ok": 1, "message": _("Thank you. We will be in touch shortly.")}

	full_name = _clean(kwargs.get("full_name"))
	business_name = _clean(kwargs.get("business_name"))
	email = _clean(kwargs.get("email"), 80)
	mobile = _clean(kwargs.get("mobile"), 24)
	country = _clean(kwargs.get("country"), 80)
	city = _clean(kwargs.get("city"), 80)
	business_type = _clean(kwargs.get("business_type"), 80)
	branches = _clean(kwargs.get("branches"), 20)
	employees = _clean(kwargs.get("employees"), 20)
	current_software = _clean(kwargs.get("current_software"), 80)
	message = _clean(kwargs.get("message"), 1000)

	if not full_name or not NAME_RE.match(full_name):
		frappe.throw(_("Please enter a valid full name."))
	if not business_name:
		frappe.throw(_("Please enter your business name."))
	if not email and not mobile:
		frappe.throw(_("Please enter a mobile number or an email address."))
	if email:
		validate_email_address(email, throw=True)
	if mobile and not PHONE_RE.match(mobile):
		frappe.throw(_("Please enter a valid mobile number."))

	loaded = _clean(kwargs.get("form_loaded_at"), 40)
	if loaded:
		try:
			started = datetime.fromisoformat(loaded.replace("Z", ""))
			if (datetime.utcnow() - started).total_seconds() < 3:
				frappe.throw(_("Please review the form before sending."))
		except ValueError:
			pass

	cache_key = f"bc-demo:{email or mobile}:{business_name.lower()}"
	if frappe.cache().get_value(cache_key):
		frappe.throw(_("This request was already received. Please wait before sending again."))
	frappe.cache().set_value(cache_key, 1, expires_in_sec=15 * 60)

	first_name, last_name = _split_name(full_name)
	notes = "\n".join(
		[
			"Source: Beau-T-Cloud Website",
			f"Business type: {business_type}" if business_type else "",
			f"Branches: {branches}" if branches else "",
			f"Employees: {employees}" if employees else "",
			f"Current software: {current_software}" if current_software else "",
			f"City: {city}" if city else "",
			f"Country: {country}" if country else "",
			f"Message: {message}" if message else "",
		]
	)
	notes = "\n".join(line for line in notes.split("\n") if line)

	if "erpnext" in frappe.get_installed_apps():
		_create_lead(
			first_name=first_name,
			last_name=last_name,
			business_name=business_name,
			email=email,
			mobile=mobile,
			city=city,
			country=country,
			employees=employees,
			notes=notes,
		)
	else:
		_create_communication(full_name, business_name, email, mobile, notes)

	return {"ok": 1, "message": _("Thank you. Our team will contact you shortly.")}


def _create_lead(first_name, last_name, business_name, email, mobile, city, country, employees, notes):
	employee_options = {"1-10", "11-50", "51-200", "201-500", "501-1000", "1000+"}
	doc = frappe.get_doc(
		{
			"doctype": "Lead",
			"first_name": first_name,
			"last_name": last_name,
			"company_name": business_name,
			"email_id": email or None,
			"mobile_no": mobile or None,
			"city": city or None,
			"status": "Lead",
			"request_type": "Product Enquiry",
			"utm_source": "Beau-T-Cloud Website",
		}
	)
	if employees in employee_options:
		doc.no_of_employees = employees
	if country and frappe.db.exists("Country", country):
		doc.country = country
	doc.insert(ignore_permissions=True)
	if notes:
		doc.add_comment("Comment", text=notes)


def _create_communication(full_name, business_name, email, mobile, notes):
	frappe.get_doc(
		{
			"doctype": "Communication",
			"communication_type": "Communication",
			"communication_medium": "Email",
			"sent_or_received": "Received",
			"subject": f"Beau-T-Cloud demo request — {business_name}",
			"content": escape_html(f"{full_name}\n{business_name}\n{email}\n{mobile}\n{notes}").replace("\n", "<br>"),
			"sender": email or "website@beautcloud.com",
			"status": "Open",
		}
	).insert(ignore_permissions=True)
