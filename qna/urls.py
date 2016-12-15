from django.conf.urls import include
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.question_list, name='question_list'),
    url(r'^qna/(?P<pk>[0-9]+)/$', views.question_detail, name='question_detail'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.question_edit, name='question_edit'),
    url(r'^new/$', views.question_new, name='question_new'),
    url(r'^(?P<pk>[0-9]+)/remove/$', views.question_remove, name='question_remove'),
]

