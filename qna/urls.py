from django.conf.urls import include
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.question_list, name='question_list'),
    url(r'^(?P<pk>\d+)/$', views.question_detail, name='question_detail'),
    url(r'^(?P<pk>\d+)/edit/$', views.question_edit, name='question_edit'),
    url(r'^new/$', views.question_new, name='question_new'),
    url(r'^(?P<pk>\d+)/remove/$', views.question_remove, name='question_remove'),
]
