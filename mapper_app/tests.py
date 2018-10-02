# -*- coding: utf-8 -*-

import json, logging
from .models import LocationMapper
from django.test import Client, TestCase
# from django.test import SimpleTestCase as TestCase    ## TestCase requires db, so if you're not using a db, and want tests, try this


log = logging.getLogger(__name__)
TestCase.maxDiff = None


class RootUrlTest( TestCase ):
    """ Checks root urls. """

    def test_root_url_no_slash(self):
        """ Checks '/root_url'. """
        response = self.client.get( '' )  # project root part of url is assumed
        self.assertEqual( 302, response.status_code )  # permanent redirect
        redirect_url = response._headers['location'][1]
        self.assertEqual(  '/info/', redirect_url )

    def test_root_url_slash(self):
        """ Checks '/root_url/'. """
        response = self.client.get( '/' )  # project root part of url is assumed
        self.assertEqual( 302, response.status_code )  # permanent redirect
        redirect_url = response._headers['location'][1]
        self.assertEqual(  '/info/', redirect_url )

    # end class RootUrlTest()


class LocationUrlTest( TestCase ):
    """ Checks url hits. """
    fixtures = [ 'location_dump.json' ]

    def test_good_simple_location_hit(self):
        """ Checks good non-space ils-code. """
        response = self.client.get( '/location_api_v2/ils_code_ANNEX/' )  # project root part of url is assumed
        # log.debug( 'response.content, ```%s```' % response.content )
        self.assertEqual( 200, response.status_code )
        las_code = json.loads( response.content )['result']['returned_las_code']
        self.assertEqual( 'QS', las_code )

    def test_not_found_location_hit(self):
        """ Checks invalid ils-code. """
        response = self.client.get( '/location_api_v2/ils_code_FOO/' )  # project root part of url is assumed
        # log.debug( 'response.content, ```%s```' % response.content )
        self.assertEqual( 404, response.status_code )

    def test_good_location_hit_with_spaces(self):
        """ Checks ils-code with spaces. """
        response = self.client.get( '/location_api_v2/ils_code_ANNEX%20HAY/' )  # project root part of url is assumed
        log.debug( 'response.content, ```%s```' % response.content )
        self.assertEqual( 200, response.status_code )
        submitted_code = json.loads( response.content )['request']['requested_ils_code']
        self.assertEqual( 'ANNEX HAY', submitted_code )
        las_code = json.loads( response.content )['result']['returned_las_code']
        self.assertEqual( 'QH', las_code )

    def test_good_location_hit_with_double_encoded_spaces(self):
        """ Checks ils-code with double-encoded spaces, which seems to be happening on dev and prod apache. """
        response = self.client.get( '/location_api_v2/ils_code_ANNEX%2520HAY/' )  # project root part of url is assumed
        log.debug( 'response.content, ```%s```' % response.content )
        self.assertEqual( 200, response.status_code )
        submitted_code = json.loads( response.content )['request']['requested_ils_code']
        self.assertEqual( 'ANNEX HAY', submitted_code )
        las_code = json.loads( response.content )['result']['returned_las_code']
        self.assertEqual( 'QH', las_code )

    # end class LocationUrlTest()
