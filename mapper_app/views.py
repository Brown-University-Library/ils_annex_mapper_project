# -*- coding: utf-8 -*-

import datetime, json, logging, os, pprint, urllib
from . import settings_app
from .models import LocationMapper, PickupAtMapper
from django.conf import settings as project_settings
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from mapper_app.lib import view_info_helper


log = logging.getLogger(__name__)


def info( request ):
    """ Returns basic data including branch & commit. """
    log.debug( 'user-agent, ```%s```; ip, ```%s```; referrer, ```%s```' %
        (request.META.get('HTTP_USER_AGENT', None), request.META.get('REMOTE_ADDR', None), request.META.get('HTTP_REFERER', None)) )
    rq_now = datetime.datetime.now()
    commit = view_info_helper.get_commit()
    branch = view_info_helper.get_branch()
    info_txt = commit.replace( 'commit', branch )
    resp_now = datetime.datetime.now()
    taken = resp_now - rq_now
    context_dct = view_info_helper.make_context( request, rq_now, info_txt, taken )
    output = json.dumps( context_dct, sort_keys=True, indent=2 )
    return HttpResponse( output, content_type='application/json; charset=utf-8' )


def location_v2( request, ils_code ):
    """ Returns json showing the annex-software `CUSTOMER_CODE` code for the given ILS `LOCATION` code. """
    log.debug( 'user-agent, ```%s```; ip, ```%s```; referrer, ```%s```' %
        (request.META.get('HTTP_USER_AGENT', None), request.META.get('REMOTE_ADDR', None), request.META.get('HTTP_REFERER', None)) )
    log.debug( 'ils_code initially, `%s`' % ils_code )
    ils_code = urllib.parse.unquote( ils_code )  # apache seems to be double-encoding
    location_mapper_record = get_object_or_404(LocationMapper, ils_code=ils_code)
    response_dct = {
        'request': {
            'requested_ils_code': ils_code
        },
        'result': {
            'definition_ils_code': 'Sierra "LOCATION" code',
            'definition_las_code': 'LAS "CUSTOMER_CODE" code',
            'returned_las_code': location_mapper_record.las_code,
            'service_documentation': settings_app.README_URL
        }
    }
    output = json.dumps( response_dct, sort_keys=True, indent=2 )
    return HttpResponse( output, content_type='application/json; charset=utf-8' )


def pickup_v2( request, ils_code ):
    """ Returns json showing the annex-software `DELIVERY STOP` code for the given ILS `PICKUP AT` code. """
    log.debug( 'user-agent, ```%s```; ip, ```%s```; referrer, ```%s```' %
        (request.META.get('HTTP_USER_AGENT', None), request.META.get('REMOTE_ADDR', None), request.META.get('HTTP_REFERER', None)) )
    ils_code = urllib.parse.unquote( ils_code )
    pickup_mapper_record = get_object_or_404(PickupAtMapper, ils_code=ils_code)
    response_dct = {
        'request': {
            'requested_ils_code': ils_code
        },
        'result': {
            'definition_ils_code': 'Sierra "PICKUP AT" code',
            'definition_las_code': 'LAS "DELIVERY STOP" code',
            'returned_las_code': pickup_mapper_record.las_code,
            'service_documentation': settings_app.README_URL
        }
    }
    output = json.dumps( response_dct, sort_keys=True, indent=2 )
    return HttpResponse( output, content_type='application/json; charset=utf-8' )


def location_all_v1( request ):
    """ Returns json showing all of the annex-software `CUSTOMER_CODE` codes and their corresponding ILS `LOCATION` codes. """
    log.debug( 'user-agent, ```%s```; ip, ```%s```; referrer, ```%s```' %
        (request.META.get('HTTP_USER_AGENT', None), request.META.get('REMOTE_ADDR', None), request.META.get('HTTP_REFERER', None)) )
    record_query = LocationMapper.objects.all().order_by( 'ils_code' )
    record_lst = []
    record_lst.append( {
        'definition_ils_code': 'Sierra "CUSTOMER_CODE" code',
        'definition_las_code': 'LAS "LOCATION" code'
    } )
    for record in record_query:
        record_lst.append( {
            'ils_code': record.ils_code,
            'las_code': record.las_code
        } )
    response_dct = {
      'request':'all_entries',
      'response':record_lst,
      'service_documentation':settings_app.README_URL
      }
    output = json.dumps( response_dct, sort_keys=True, indent=2 )
    return HttpResponse( output, content_type='application/json; charset=utf-8' )


def pickup_all_v1( request ):
    """ Returns json showing all of the annex-software `DELIVERY STOP` codes and their corresponding ILS `PICKUP AT` codes. """
    log.debug( 'user-agent, ```%s```; ip, ```%s```; referrer, ```%s```' %
        (request.META.get('HTTP_USER_AGENT', None), request.META.get('REMOTE_ADDR', None), request.META.get('HTTP_REFERER', None)) )
    record_query = PickupAtMapper.objects.all().order_by( 'ils_code' )
    record_lst = []
    record_lst.append( {
        'definition_ils_code': 'Sierra "PICKUP AT" code',
        'definition_las_code': 'LAS "DELIVERY STOP" code'
    } )
    for record in record_query:
        record_lst.append( {
            'ils_code': record.ils_code,
            'las_code': record.las_code
        } )
    response_dct = {
      'request':'all_entries',
      'response':record_lst,
      'service_documentation':settings_app.README_URL
      }
    output = json.dumps( response_dct, sort_keys=True, indent=2 )
    return HttpResponse( output, content_type='application/json; charset=utf-8' )
