"use strict";
$(document).ready(function($) {
	$('.customers').ready(function() {
		var currentCustomer = $('.customers option:disabled').val();

		$.getJSON('/ajax/sort/second/', {customersName: currentCustomer, csrfmiddlewaretoken: '{{ csrf_token }}'}, function(json, textStatus) {
			var customers = $.parseJSON(json);
			var select = $('.customers');
			var table = $('.result');
			
			for(let i = 0; i < customers.length; i++) {
				select.append($('<option />').val(customers[i].fields.orders_customer).text(customers[i].fields.orders_customer));
				table.append('<tr><td>' + customers[i].fields.orders_id + '</td><td>' + customers[i].fields.orders_product + '</td><td>' + customers[i].fields.orders_quantity + '</td><td>' + customers[i].fields.orders_customer + '</td></tr>');
			}
		});
	});


	$('.sort').submit(function(event) {
		var currentCustomer = $('.customers option:selected').val();

		$.getJSON('/ajax/sort/second/', {customersName: currentCustomer, csrfmiddlewaretoken: '{{ csrf_token }}'}, function(json, textStatus) {
			var customers = $.parseJSON(json);
			var element = $('.result');
			element.find('tr:gt(0)').remove();

			for(let i = 0; i < customers.length; i++) {
				element.append('<tr><td>' + customers[i].fields.orders_id + '</td><td>' + customers[i].fields.orders_product + '</td><td>' + customers[i].fields.orders_quantity + '</td><td>' + customers[i].fields.orders_customer + '</td></tr>');
			}
		});
		return false;
	});

})