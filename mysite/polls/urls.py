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
from . import views

app_name = 'polls'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(),name='index'),
# 
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'), 

    url(r'^(?P<pk>[0-9]+)/results/$',views.ResultsView.as_view(),name='results'), 

    url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote,name='vote'), 

    url(r'^getname$',views.get_name,name='getname'), 

    url(r'^register$',views.register),

    url(r'^login$',views.login3,name='login'),

    url(r'^logout$',views.logout,name='logout'),

    url(r'^upload$',views.upLoad,name='upload'),
    
] 
