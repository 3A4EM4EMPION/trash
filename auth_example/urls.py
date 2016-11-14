from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'main/$', views.render_page, {}),
	url(r'login/$', views.user_login, {}),
	url(r'logout/$', views.user_logout, {}),
	url(r'signup/$', views.user_signup, {}),
]