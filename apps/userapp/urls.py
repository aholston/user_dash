from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^reginfo$', views.reginfo),
    url(r'^register$', views.register),
    url(r'^signin$', views.signin),
    url(r'^$', views.index)
]
