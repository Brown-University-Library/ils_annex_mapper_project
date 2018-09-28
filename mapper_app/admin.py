# -*- coding: utf-8 -*-

from .models import LocationMapper, PickupAtMapper
from django.contrib import admin


class LocationMapperAdmin( admin.ModelAdmin ):
    list_display = [ 'ils_code', 'las_code', 'notes', 'modify_date' ]
    ordering = [ 'ils_code' ]
    save_on_top = True

class PickupAtMapperAdmin( admin.ModelAdmin ):
    list_display = [ 'ils_code', 'las_code', 'notes', 'modify_date' ]
    ordering = [ 'ils_code' ]
    save_on_top = True


admin.site.register( LocationMapper, LocationMapperAdmin )
admin.site.register( PickupAtMapper, PickupAtMapperAdmin )
