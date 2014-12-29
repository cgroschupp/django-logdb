from django.conf import settings
from django.conf.urls import patterns
from django.contrib import admin

from djangologdb import settings as djangologdb_settings
from djangologdb import views

urlpatterns = patterns('',
    (r'datasets/$', admin.site.admin_view(views.datasets)),
)
