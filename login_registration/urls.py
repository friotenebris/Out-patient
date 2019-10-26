from django.conf.urls import url, include
from django.contrib import admin
urlpatterns = [
    url(r'^appPage', include('apps.register.urls')),
    url('admin/', admin.site.urls),
]
