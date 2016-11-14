from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings

import Article
import ajax_example


from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^article/', include('Article.urls')),
    url(r'^ajax/', include('ajax_example.urls')),
    url(r'^auth/', include('auth_example.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)