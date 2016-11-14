"use strict";
$(document).ready(function($) {
	$.getJSON('/ajax/db/res/', function(json, textStatus) {
			var city = $("#city");
			var country = $('#country');
			var region = $('#region');

			var result = $.parseJSON(json);

			for(var i = 0; i < result.length; i++){
				city.append($('<option />').text(result[i].fields.city_info_city));
				country.append($('<option />').text(result[i].fields.city_info_country));
				region.append($('<option />').text(result[i].fields.city_info_region));
			}
	});

});