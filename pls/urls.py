"""pls URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf.urls.static import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # packages
    url(r'^summernote/', include('django_summernote.urls')),

    # for admin
    url(r'^admin/', include(admin.site.urls)),

    # for user
    url(r'^qna/', include('qna.urls')),
    url(r'', include('qna.urls')),

]

# django-summernote image upload
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

# Change Admin site header
admin.site.site_header = 'PL센터 관리자'
