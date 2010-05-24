#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by carlo on 2009-09-19.
Copyright (c) 2009 Carlo Bifulco. All rights reserved.
"""

import sys
import os
import sys

sys.path = sys.path + ['/usr/local/google_appengine', '/usr/local/google_appengine/lib/django', '/usr/local/google_appengine/lib/webob', '/usr/local/google_appengine/lib/yaml/lib', '/usr/local/google_appengine/google/appengine']
 
from google.appengine.api import apiproxy_stub_map
from google.appengine.api import datastore_file_stub
from google.appengine.api import mail_stub
from google.appengine.api import urlfetch_stub
from google.appengine.api import user_service_stub
 
APP_ID = u'test_app'
AUTH_DOMAIN = 'gmail.com'
LOGGED_IN_USER = 'carlobif@gmail.com'  # set to '' for no logged in user
 
# Start with a fresh api proxy.
apiproxy_stub_map.apiproxy = apiproxy_stub_map.APIProxyStubMap()
 
# Use a fresh stub datastore.
stub = datastore_file_stub.DatastoreFileStub(APP_ID, '/dev/null', '/dev/null')
apiproxy_stub_map.apiproxy.RegisterStub('datastore_v3', stub)
 
# Use a fresh stub UserService.
apiproxy_stub_map.apiproxy.RegisterStub('user',
user_service_stub.UserServiceStub())
os.environ['AUTH_DOMAIN'] = AUTH_DOMAIN
os.environ['USER_EMAIL'] = LOGGED_IN_USER
 
# Use a fresh urlfetch stub.
apiproxy_stub_map.apiproxy.RegisterStub(
    'urlfetch', urlfetch_stub.URLFetchServiceStub())
 
# Use a fresh mail stub.
apiproxy_stub_map.apiproxy.RegisterStub(
  'mail', mail_stub.MailServiceStub())


def main():
  pass


if __name__ == '__main__':
  main()

