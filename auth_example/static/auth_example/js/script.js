"use strict"
$(document).ready(function(){
	$("#login").submit(function(event) {
		var currentLogin = $('#login input:text[name=login]').val();
		var currentPass = $('#login input:password[name=pass]').val();
		$.ajax({
			url: '/auth/login/',
			data: {
					login: currentLogin, 
					password: currentPass,
				},
			success: function(responce){
				if(responce){
					$('.username h1').text(responce);
					$('#login, .login, .signup').addClass('hidden');
					$('.decoration, .logout').removeClass('hidden');
				} else{
					$('.modal-error-login').text('Error! Try again!');
				}
			},
		});
		return false;
	});

	$("#signup").submit(function(event) {
		var currentLogin = $('#signup input:text[name=login]').val();
		var currentPass = $('#signup input:password[name=pass]').val();
		var currentEmail = $('#signup input:text[name=email]').val();
		$.ajax({
			url: '/auth/signup/',
			data: {
					login: currentLogin, 
					password: currentPass,
					email: currentEmail,
				},
			success: function(responce){
				if(responce){
					$('.decoration, .logout').removeClass('hidden');
					$('#signup, .login, .signup').addClass('hidden');
				} else{
					$('.modal-error-signup').text('Error! Try again!');
				}
			},
		});
		return false;
	});
});