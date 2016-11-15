from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.article_list, name='aarticle_list'),
    url(r'^(?P<article_id>\d{1})$', views.article_details, name='article_details'),
]
