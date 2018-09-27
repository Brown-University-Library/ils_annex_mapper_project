# -*- coding: utf-8 -*-

from .models import LocationMapper, PickupAtMapper
from django.contrib import admin


class LocationMapperAdmin( admin.ModelAdmin ):
    list_display = [ 'ils_code' ]
    # ordering = [ '-count_date' ]


admin.site.register( LocationMapper, LocationMapperAdmin )
