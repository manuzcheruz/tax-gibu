from django.conf.urls import url
from .views import *
from . import views

urlpatterns = [
    url(r'^$', views.home_page, name="HomePage"),
    url(r'^app-ads.txt$', views.ads, name="ads"),
]
