"use strict"
jQuery(document).ready(function($) {
	setTimeout(function() {
		$.ajax({
				url: '/path/to/f/ajax/sort/3/',
		})
		.done(function() {
			console.log("success");
		})
		.fail(function() {
			console.log("error");
		})
		.always(function() {
			console.log("complete");
		});
	}, 2000);
});