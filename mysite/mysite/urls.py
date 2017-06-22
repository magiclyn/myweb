"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
    #     'document_root': settings.MEDIA_ROOT
    #     }),
    # (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
    # 'document_root': settings.MEDIA_ROOT
    #     }),


    url(r'^admin/', admin.site.urls),
    url(r'^$', views.hello),
    url(r'^contact', views.contact),
    url(r'^index.html', views.hello),
    url(r'^description.htm', views.description),
    url(r'^features.html', views.features),
    url(r'^pricing.html', views.pricing),
    url(r'^tour.html', views.tour),
    url(r'^polls/',include('polls.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
