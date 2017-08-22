$(function () {

	/* Functions */

	var loadForm = function () {
		var btn = $(this);
		$.ajax({
			url: btn.attr("data-url"),
			type: 'get',
			dataType: 'json',
			beforeSend: function () {
				$("#message-box-warning").modal("show");
			},
			success: function (data) {
				$("#message-box-warning .mb-container").html(data.html_form);
			}
		});
	};

	var saveForm = function () {
		var form = $(this);
		$.ajax({
			url: form.attr("action"),
			data: form.serialize(),
			type: form.attr("method"),
			dataType: 'json',
			success: function (data) {
				if (data.form_is_valid) {
					$("#tabela tbody").html(data.html_list);
					$("#message-box-warning").modal("hide");
				} else {
					$("#message-box-warning .mb-container").html(data.html_form);
				}
			}
		});
		return false;
	};

	// Delete book
	$("#tabela").on("click", ".js-delete-book", loadForm);
	$("#message-box-warning").on("submit", ".js-book-delete-form", saveForm);
});