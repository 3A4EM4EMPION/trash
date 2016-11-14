"use strict"
$(document).ready(function($) {
	$('.button1').click(function(event) {
		$.ajax({
			url: '/ajax/sort/first/',
			dataType: 'json',
			data: {
					startValue: 0,
					endValue: 5,
					csrfmiddlewaretoken: '{{ csrf_token }}',
				},
			success: function(responce) {
				
				var result = $.parseJSON(responce);
				for(let i = 0; i < result.length; i++) {
					$('.result').append('<li>' + result[i].fields.city_info_region + '</li>');
				}
			}
		})
	});

	$('.button2').click(function(event) {
		$.getJSON('/ajax/sort/first/', {startValue: 5, endValue: 10, srfmiddlewaretoken: '{{ csrf_token }}',}, function(json, textStatus) {
			
			var result = $.parseJSON(json);
			for(let i = 0; i < result.length; i++) {
				$('.result').append('<li>' + result[i].fields.city_info_region + '</li>');
			}
		});
	});

	$('.button3').click(function(event) {
		$.getJSON('/ajax/sort/first/', {startValue: 10, endValue: 15, srfmiddlewaretoken: '{{ csrf_token }}',}, function(json, textStatus) {
			
			var result = $.parseJSON(json);
			for(let i = 0; i < result.length; i++) {
				$('.result').append('<li>' + result[i].fields.city_info_region + '</li>');
			}
		});

	});
});