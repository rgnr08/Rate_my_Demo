from django.conf.urls import patterns, url
from Rate_my_Demo import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^artist/$', views.artist, name='artist'),
        url(r'^listener/$', views.listener, name='listener'),
        url(r'^home/$', views.home, name='home'),
        url(r'^about_page/$', views.about, name='about'),
        url(r'^registration_successful/$', views.reg_success, name='about'),
        url(r'^bad_details/$', views.about, name='about'),
        url(r'^register_page/$', views.register, name='register_page'),
        url(r'^login_page/$', views.user_login, name='login_page'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^check_usertype/$', views.check_usertype, name='check_usertype'),
        url(r'^upload_page/$', views.upload, name='upload'),
        url(r'^contact/$', views.contact, name='contact'),
        url(r'^demos/$', views.demos, name='demos'),
        url(r'^favourites/$', views.favourites, name='favourites'),
        url(r'^listener_favourites/$', views.listener_favourites, name='favourites'),
        url(r'^user_details/$', views.user_details, name='user-details'),
        url(r'^like_demo/$', views.like_demo, name='like_demo'),
        url(r'^unlike_demo/$', views.unlike_demo, name='unlike_demo'),

        # url(r'^list/$', views.list, name='list'),




        #url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/favicon.ico'}),
        )
