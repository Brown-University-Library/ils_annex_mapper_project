# -*- coding: utf-8 -*-

import datetime, json, logging, os, pprint
from django.conf import settings as project_settings
from django.core.urlresolvers import reverse
from django.db import models
from django.http import HttpResponseRedirect


log = logging.getLogger(__name__)


class LocationMapper(models.Model):
    create_date = models.DateTimeField( auto_now_add=True, help_text='Set automatically on save.' )
    modify_date = models.DateTimeField( auto_now=True, help_text='Set automatically on save.' )
    ils_code = models.CharField( max_length=50, help_text='This is the Josiah `Location` code.' )
    las_code = models.CharField( max_length=50, help_text='This the the LAS `Customer Code` code.' )
    notes = models.TextField( blank=True )

    ## end class LocationMapper()


class PickupAtMapper(models.Model):
    create_date = models.DateTimeField( auto_now_add=True, help_text='Set automatically on save.' )
    modify_date = models.DateTimeField( auto_now=True, help_text='Set automatically on save.' )
    ils_code = models.CharField( max_length=50, help_text='This is the Josiah `Pickup At` code.' )
    las_code = models.CharField( max_length=50, help_text='This the the LAS `Customer Code` code.' )
    notes = models.TextField( blank=True )

    ## end class PickupAtMapper()
