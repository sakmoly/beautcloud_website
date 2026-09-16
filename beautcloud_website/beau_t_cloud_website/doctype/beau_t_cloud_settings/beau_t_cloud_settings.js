frappe.ui.form.on("Beau-T-Cloud Settings", {
	refresh(frm) {
		frm.set_intro(
			"These values appear on the public Beau-T-Cloud website. Screenshot previews use a 16:10 screen (1440 × 900 px). Leave a screenshot empty to keep the branded product preview."
		);
		frm.fields
			.filter((field) => field.df.fieldname && field.df.fieldname.endsWith("_screenshot"))
			.forEach((field) => {
				const $link = field.$value && field.$value.find(".attached-file-link");
				if (!$link || !$link.length || !$link.data("bs.popover")) {
					return;
				}
				$link.popover("dispose");
				$link.popover({
					trigger: "hover",
					placement: "bottom",
					content: () =>
						`<div><img src="${field.get_value()}" width="720" style="object-fit:contain;max-width:720px;aspect-ratio:16/10;" /></div>`,
					html: true,
				});
			});
	},
});
