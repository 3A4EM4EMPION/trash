(function(){
	$('#sum').submit(function(){
		var values = $(this).serialize();
		$.ajax({
			type:'POST',
			url:'/ajax/math/sum/',
			data: values,
			success: function(response){
				$('.sum_res').html(response);
			}
		});
		return false;
	})

	$('#dif').submit(function(){
		var values = $(this).serialize();
		$.post('/ajax/math/dif/', {data:values,}
}, 
			function(data, textStatus, xhr) {
				$('.dif_res').html(data);
		});
		return false;
	})

	$('#mult').submit(function(){
		var values = $(this).serialize();
		$.ajax({
			type:'POST',
			url:'/ajax/math/mult/',
			data: values,
			success: function(response){
				$('.mult_res').html(response);
			}
		});
		return false;
	})

	$('#div').submit(function(){
		var values = $(this).serialize();
		$.ajax({
			type:'POST',
			url:'/ajax/math/div/',
			data: values,
			success: function(response){
				$('.div_res').html(response);
			}
		});
		return false;
	})
})()