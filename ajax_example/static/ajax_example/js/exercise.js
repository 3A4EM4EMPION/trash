$('.button1').click(function(event) {
	$.ajax({
		url: '/ajax/change/',
		cache: false,
		success: function(response){
			$('.content').html(response);
		}
	})
});

$('.button2').click(function(event) {
	$.get('/ajax/change/', function(response){
			$('.content').html(response).css({'color':'red'});
		})
});

$('.button3').click(function(event) {
	$('.content').load('/ajax/change/', function(response){
			$('.content').css({'color':'green'});
		})
});