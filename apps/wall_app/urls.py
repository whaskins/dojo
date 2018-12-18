from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.wall),
    url(r'^/make_message$', views.make_message),
    url(r'^/make_comment$', views.make_comment),
]
