from django.conf.urls import url
from .views import *
from . import views

urlpatterns = [
    url(r'^$', views.home_page, name="HomePage"),
    url(r'^app-ads.txt$', views.ads, name="ads"),
    url(r'^privacy-policy$', views.privacy_policy, name="privacy"),
    url(r'^privacy-policy2$', views.privacy_policy2, name="privacy2"),
]