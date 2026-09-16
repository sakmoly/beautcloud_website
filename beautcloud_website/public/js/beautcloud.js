(function () {
	function ready(fn) {
		if (document.readyState === "loading") {
			document.addEventListener("DOMContentLoaded", fn);
		} else {
			fn();
		}
	}

	function setLang(lang) {
		const html = document.documentElement;
		html.lang = lang;
		html.dir = lang === "ar" ? "rtl" : "ltr";
		document.querySelectorAll("[data-bc-lang]").forEach(function (btn) {
			btn.classList.toggle("is-active", btn.getAttribute("data-bc-lang") === lang);
			btn.setAttribute("aria-pressed", btn.getAttribute("data-bc-lang") === lang ? "true" : "false");
		});
		try {
			localStorage.setItem("bc_lang", lang);
			document.cookie = "preferred_language=" + lang + ";path=/;max-age=31536000";
		} catch (e) {
			/* ignore */
		}
	}

	ready(function () {
		const nav = document.querySelector(".bc-nav");
		const burger = document.querySelector("[data-bc-burger]");
		const menu = document.querySelector("[data-bc-menu]");

		if (nav) {
			const onScroll = function () {
				nav.classList.toggle("is-compact", window.scrollY > 12);
			};
			onScroll();
			window.addEventListener("scroll", onScroll, { passive: true });
		}

		if (burger && menu) {
			burger.addEventListener("click", function () {
				const open = nav.classList.toggle("is-open");
				burger.setAttribute("aria-expanded", open ? "true" : "false");
			});
		}

		document.querySelectorAll("[data-bc-drop]").forEach(function (btn) {
			btn.addEventListener("click", function () {
				const item = btn.closest("li");
				const willOpen = !item.classList.contains("is-open");
				document.querySelectorAll(".bc-menu > li.is-open").forEach(function (openItem) {
					openItem.classList.remove("is-open");
					const toggle = openItem.querySelector("[data-bc-drop]");
					if (toggle) toggle.setAttribute("aria-expanded", "false");
				});
				item.classList.toggle("is-open", willOpen);
				btn.setAttribute("aria-expanded", willOpen ? "true" : "false");
			});
		});

		document.addEventListener("keydown", function (event) {
			if (event.key === "Escape" && nav) {
				nav.classList.remove("is-open");
				document.querySelectorAll(".bc-menu > li.is-open").forEach(function (item) {
					item.classList.remove("is-open");
				});
			}
		});

		let lang = "en";
		try {
			lang = localStorage.getItem("bc_lang") || "en";
		} catch (e) {
			lang = "en";
		}
		setLang(lang);
		document.querySelectorAll("[data-bc-lang]").forEach(function (btn) {
			btn.addEventListener("click", function () {
				setLang(btn.getAttribute("data-bc-lang"));
			});
		});

		const form = document.querySelector("[data-bc-demo-form]");
		if (form) {
			const loaded = form.querySelector("[name='form_loaded_at']");
			if (loaded) loaded.value = new Date().toISOString();
			form.addEventListener("submit", function (event) {
				event.preventDefault();
				const status = form.querySelector("[data-bc-form-status]");
				const button = form.querySelector("[type='submit']");
				const payload = {};
				new FormData(form).forEach(function (value, key) {
					payload[key] = value;
				});
				if (status) {
					status.textContent = "Sending…";
					status.className = "bc-form-status";
				}
				if (button) button.disabled = true;
				if (!(window.frappe && frappe.call)) {
					if (status) {
						status.textContent = "Form service is not ready. Please refresh and try again.";
						status.className = "bc-form-status is-err";
					}
					if (button) button.disabled = false;
					return;
				}
				frappe.call({
					method: "beautcloud_website.api.demo.submit_demo",
					args: payload,
					callback: function (res) {
						const message =
							(res && res.message && res.message.message) || "Thank you. We will be in touch shortly.";
						if (status) {
							status.textContent = message;
							status.className = "bc-form-status is-ok";
						}
						form.reset();
						if (loaded) loaded.value = new Date().toISOString();
					},
					error: function (err) {
						const server =
							err && err._server_messages
								? err._server_messages
								: (err && err.message) || "Please check the form and try again.";
						if (status) {
							status.textContent = typeof server === "string" ? server.replace(/<[^>]+>/g, "") : "Please check the form and try again.";
							status.className = "bc-form-status is-err";
						}
					},
					always: function () {
						if (button) button.disabled = false;
					},
				});
			});
		}
	});
})();
