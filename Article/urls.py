from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.articles),
    url(r'^(?P<article_id>\d{1})$', views.full_article),  
]