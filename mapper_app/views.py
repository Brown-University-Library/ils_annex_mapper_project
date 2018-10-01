# -*- coding: utf-8 -*-

import datetime, json, logging, os, pprint
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
    # log.debug( 'request.__dict__, ```%s```' % pprint.pformat(request.__dict__) )
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
    """ Returns json showing the annex-software `DELIVERY STOP` code for the given ILS `PICKUP AT` code. """
    location_mapper_record = get_object_or_404(LocationMapper, ils_code=ils_code)
    response_dct = {
        'request': {
            'requested_ils_code': ils_code
        },
        'result': {
            'definition_ils_code': 'Sierra "PICKUP AT" code',
            'definition_las_code': 'LAS "DELIVERY STOP" code',
            'returned_las_code': location_mapper_record.las_code,
            'service_documentation': settings_app.README_URL
        }
    }
    output = json.dumps( response_dct, sort_keys=True, indent=2 )
    return HttpResponse( output, content_type='application/json; charset=utf-8' )


def pickup_v2( request, ils_code ):
    """ Returns json showing the annex-software `DELIVERY STOP` code for the given ILS `PICKUP AT` code. """
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
