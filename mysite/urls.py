from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.auth.views import logout
from time_system.views import *
admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),
    (r'^home/$' , home),
    (r'^(\d{1,2})/$', eack_pack) ,
    (r'^newPack/$' , add_task_packet),
    (r'^add_new_task/$' , add_new_task),
    (r'^end(\d{1,2})/$' , end_pack),
    # (r'^accounts/login/$', my_login),
    (r'^logout/$', my_logout),
    (r'^login/$',  my_login),
    (r'^$' , my_login),
    (r'^register/$' , my_register),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

)
