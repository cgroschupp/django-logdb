from django.conf.urls import url
from django.conf import settings
from django.contrib import admin

from djangologdb import settings as djangologdb_settings
from djangologdb import views

urlpatterns = [
    url(r'datasets/$', admin.site.admin_view(views.datasets)),
]
