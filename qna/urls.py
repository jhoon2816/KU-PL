from django.conf.urls import include
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.question_list, name='question_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.question_detail, name='question_detail'),
]
