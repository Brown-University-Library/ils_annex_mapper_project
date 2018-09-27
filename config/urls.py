# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView
from mapper_app import views


admin.autodiscover()


urlpatterns = [

    url( r'^admin/', admin.site.urls ),  # eg host/project_x/admin/
    # url( r'^admin/', include(admin.site.urls) ),

    url( r'^info/$', views.info, name='info_url' ),

    url( r'^location_api_v2/ils_code_(?P<ils_code>.*)/$',  views.location_v2, name='location_v2_url' ),

    url( r'^pickup_api_v2/ils_code_(?P<ils_code>.*)/$',  views.pickup_v2, name='pickup_v2_url' ),

    url( r'^$', RedirectView.as_view(pattern_name='info_url') ),

    ]
