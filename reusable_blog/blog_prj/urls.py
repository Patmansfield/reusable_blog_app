from django.conf.urls import include, url
from django.contrib import admin
from blog import views
from django.views.static import serve
from .settings import MEDIA_ROOT


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
    url(r'^blog/$', views.post_list),
    url(r'^blog/(?P<id>\d+)/$', views.post_detail),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
]
