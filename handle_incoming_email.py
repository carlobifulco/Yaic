#!/usr/bin/env python
# encoding: utf-8
"""
handle_incoming_email.py

Created by carlo bifulco on 2009-10-26.
Copyright (c) 2009 CBB inc.. All rights reserved.
"""

import sys
import os
import  google.appengine.ext.webapp.mail_handlers
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import memcache
from mako.template import Template as mako_template
#from web_publish import TemplatedPage
import web_publish
#from google.appengine.ext.webapp.mail_handlers import InboundEmailMessage



class OrderParser:
  def __init__(self,order):
    order=order.split()
    self.quantity=order[2]
    self.ticker=order[3]
    self.action=order[1]
    self.price=order[7]
    if action=="SOLD":
      self.sell()
    if action=="BOT":
      self.buy()
      
  def sell(self):
    pass
  def buy(self):
    pass
    
    
class EmailHandler(InboundMailHandler,web_publish.MakoTemplatedPage):
  """Handler class for all email activity."""
  
  def get(self):
    #global PICASA_CLIENT
    print "SDSDS"

  def receive(self, message=None):
    """Handles /tellme requests, asking the Guru a question."""
    print message
    memcache.set(key="sender", value=message.sender, time=3600)
    memcache.set(key="subject", value=message.subject, time=3600)
    memcache.set(key="to", value=message.to, time=3600)
    memcache.set(key="bodies", value=message.bodies, time=3600)
    memcache.set(key="attachments", value=message.attachments, time=3600)
    print "sdsdsd"



def main():
  application = webapp.WSGIApplication([
      ('/_ah/mail/.+ ', EmailHandler)], debug=True)


