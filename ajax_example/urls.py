from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.page_render, {'template': 'ajax_main.html'}),
	url(r'^change/', views.page_render, {'template': 'changes.html'}),
	url(r'^math/$', views.page_render, {'template': 'math_post.html'}),
	url(r'^math/(?P<type>\w+)/$', views.ajax_math_responce,),
	url(r'^db/$', views.page_render, {'template': 'data_base.html'}),
	url(r'^db/res/$', views.ajax_data_base_responce),

	url(r'^sort/1/$', views.page_render, {'template': 'sort_first.html'}),
	url(r'^sort/first/$', views.ajax_sort_responce_first),

	url(r'^sort/2/$', views.page_render, {'template': 'sort_second.html'}),
	url(r'^sort/second/$', views.ajax_sort_responce_second),

	url(r'^sort/3/$', views.page_render, {'template': 'sort_third.html'}),
	url(r'^sort/third/$', views.ajax_sort_responce_third),
]