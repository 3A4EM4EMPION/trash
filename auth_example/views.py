from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User


def render_page(request):
	return render(request, 'signup.html', {
											'username': auth.get_user(request).username,
											})


def user_login(request):
	if request.is_ajax():
		password = request.GET.get('password', None)
		login = request.GET.get('login', None)
		user = auth.authenticate(username=login, password=password)
		if user is not None:
			auth.login(request, user)
			return HttpResponse(user.username)
		else:
			return HttpResponse()


def user_logout(request):
	if request.user.is_authenticated:
		auth.logout(request)
		return HttpResponseRedirect('/auth/main/')
	else:
		pass


def user_signup(request):
	if request.is_ajax():
		password = request.GET.get('password', None)
		login = request.GET.get('login', None)
		email = request.GET.get('email', None)
		new_user = User.objects.create_user(username=login, email=email, password=password)
		if new_user is not None:
			new_user.save()
			return HttpResponse('1')
		else:
			return HttpResponse()