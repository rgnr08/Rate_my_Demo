from django.conf.urls import patterns, url
from Rate_my_Demo import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^artist_page/$', views.artist, name='artist_page'),
        url(r'^about_page/$', views.about, name='about'),
        url(r'^registration_successful/$', views.reg_success, name='about'),
        url(r'^bad_details/$', views.about, name='about'),
        url(r'^register_page/$', views.register, name='register_page'),
        url(r'^login_page/$', views.user_login, name='login_page'),
        url(r'^restricted/$', views.restricted, name='restricted'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^check_usertype/$', views.check_usertype, name='check_usertype'),
        url(r'^upload_page/$', views.upload, name='upload'),
        url(r'^contact/$', views.contact, name='contact'),
        url(r'^demos/$', views.demos, name='demos'),
        url(r'^favourites/$', views.favourites, name='favourites'),

        # url(r'^list/$', views.list, name='list'),




        #url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/favicon.ico'}),
        )
