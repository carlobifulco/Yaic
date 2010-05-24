#!/usr/bin/env python
# encoding: utf-8
"""
web_data.py

Created by carlo Bifulco on 2009-01-23.
Copyright (c) 2009 __MyCompanyName__. All rights reserved.
"""



from google.appengine.ext import db
from datetime import date
from utilities import now_pacific_day
from google.appengine.ext.webapp import template
from google.appengine.ext.db import djangoforms
import pywapi
from graph import SimpleLineTempChart
#from google.appengine.tools import bulkloader


cities_states=[("Portland","OR",0),
                ("Woodbridge","CT",4),
                ("Florence","IT",12),
                ("Caracas","VE",3),
                ("Cagliari","IT",12)]
                
main_city="Portland"

class CityPairs(object):
  def __init__(self):
    self.last=0
    self.cities_pairs=[(main_city,i) for i in [x[0] for x in cities_states if x[0]!= main_city]]
  def __iter__(self):
    return self
  def next(self):
    last=self.last
    self.last+=1
    if last+1<=len(self.cities_pairs):
      return self.cities_pairs[last]
    else:
      raise StopIteration
    
    
    
                
def get_city_delta(city):
  """
  >>> get_city_delta("Woodbridge")
  4
  """
  if city in [i[0] for i in cities_states]:
    return [i[2] for i in cities_states if city in i][0]
  else:
     return False
                
                
def update_temps():
  """returns {city:temp,...} """
  data={}
  for entry in cities_states:
    city=entry[0]
    state=entry[1]
    data[city]=Weather(city,state).get_temperature()
  return data

class Weather(object):
  def __init__(self, city, state):
    self.result = pywapi.get_weather_from_google("%s,%s" %(city,state))
  def get_temperature(self):
    """
    >>> len([Weather(couple[0],couple[1]).get_temperature() for couple in cities_states])==len(cities_states)
    True
    """
    return self.result['current_conditions']['temp_c']


class TemperatureArchiver(db.Model):
  city=db.StringProperty(default="")
  temps=db.ListProperty(basestring)
  
  @staticmethod
  def get_city(city_name):
    """get a city, and if not available,make a new one"""
    q=db.GqlQuery("SELECT * FROM TemperatureArchiver"+
                        " WHERE  city = :city",
                         city=city_name)
    result=q.fetch(1)
    if result:
      return q.fetch(1)[-1]
    else:
      city_obj=TemperatureArchiver()
      city_obj.city=city_name
      city_obj.temps=[]
      city_obj.put()
      return city_obj
  
      
  @staticmethod
  def update_temps():
    "update all temps and store them"
    cities_temps_dict=update_temps()
    for city in cities_temps_dict:
      city_obj=TemperatureArchiver.get_city(city)
      temps=city_obj.temps
      temps.append(cities_temps_dict[city])
      city_obj.temps=temps
      city_obj.put()
      
  
  @staticmethod
  def get_cities_temp_dict():
    """returns {city:temps_list,...}"""
    results={}
    q=db.GqlQuery("SELECT * FROM TemperatureArchiver")
    for city in q:
      results[city.city]=[int(i) for i in city.temps]
    return results
       
def get_temp_diff(city_a, city_b):
  cities_temps=TemperatureArchiver.get_cities_temp_dict()
  delta=get_city_delta(city_b)-get_city_delta(city_a)
  if cities_temps.has_key(city_a) and cities_temps.has_key(city_b):
    data=[(i[0]-i[1])for i in zip(cities_temps[city_a][delta:],cities_temps[city_b])]
    return data
  else:
    return False


    
  



def main():
  pass


if __name__ == '__main__':
  import doctest
  doctest.testmod()


