# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView
from mapper_app import views


admin.autodiscover()


urlpatterns = [

    url( r'^admin/login/', RedirectView.as_view(pattern_name='login_url') ),
    url( r'^admin/', admin.site.urls ),
    url( r'^login/$', views.login, name='login_url' ),

    url( r'^info/$', views.info, name='info_url' ),

    url( r'^location_api_v1/all/$',  views.location_all_v1, name='location_all_v1_url' ),
    url( r'^pickup_api_v1/all/$',  views.pickup_all_v1, name='pickup_all_v1_url' ),

    url( r'^location_api_v2/ils_code_(?P<ils_code>.*)/$',  views.location_v2, name='location_v2_url' ),
    url( r'^pickup_api_v2/ils_code_(?P<ils_code>.*)/$',  views.pickup_v2, name='pickup_v2_url' ),

    url( r'^$', RedirectView.as_view(pattern_name='info_url') ),

    ]
