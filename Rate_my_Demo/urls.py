from django.conf.urls import patterns, url
from Rate_my_Demo import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^restricted/$', views.restricted, name='restricted'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^upload/$', views.upload, name='upload'),



        #(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/favicon.ico'}),
        )
