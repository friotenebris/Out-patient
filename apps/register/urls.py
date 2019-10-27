from django.conf.urls import url
# from apps import views
from django.contrib import admin
from apps.register import views
urlpatterns = [
    url(r'^$',views.index),
    url(r'^register$',views.register),
    url(r'^success$',views.success),
    url(r'^login$',views.login),
    url(r'^doctor$',views.doctor,name='doctor'),
    url(r'^main$',views.main_page),
    #url('admin/', admin.site.urls),
]
