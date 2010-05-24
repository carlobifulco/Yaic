#!/usr/bin/env python
# encoding: utf-8
"""
utilities.py

Created by carlo bifulco on 2009-07-10.
Copyright (c) 2009 __MyCompanyName__. All rights reserved.
"""

import sys
import os
from datetime import datetime as datetime_module
import datetime
import pytz
pacific = pytz.timezone('US/Pacific')




def now_pacific_time():
  utc_time=datetime.datetime.utcnow()
  utc_time=datetime.datetime(utc_time.year,utc_time.month,utc_time.day,utc_time.hour,utc_time.minute, tzinfo=pytz.utc)
  return utc_time.astimezone(pacific)

def now_pacific_day():
  pt=now_pacific_time()
  return datetime.date(pt.year,pt.month,pt.day)
  
  
  
  
  
  return datetime.date.today()+datetime.timedelta(hours=8)

def odd(list_array):
  """
  In [35]: odd([1,2,3,4,5,6,7])
  Out[35]: [1, 3, 5, 7]
  """
  return [i for i in list_array if list_array.index(i)%2==0]

def even(list_array):
  """
  In [36]: even([1,2,3,4,5,6,7])
  Out[36]: [2, 4, 6]
  """
  return [i for i in list_array if list_array.index(i)%2!=0]  
  
def make_even_pairs_list(list_array):
  """
  In [78]: make_even_pairs_list([1,2])
  Out[78]: [(1, 2), ('', '')]

  In [79]: make_even_pairs_list([1,2,3,4])
  Out[79]: [(1, 2), (3, 4)]

  """
  odd_members=odd(list_array)
  even_members=even(list_array)
  if len(odd_members)<len(even_members):
    odd_members.append("")
  if len(even_members)<len(odd_members):
    even_members.append("")
  pairs_list=zip(odd_members,even_members)
  if len(pairs_list)%2!=0:
    pairs_list.append(("",""))
  return pairs_list


def clean_none_from_list(a_list):
  """In [240]: clean_none_from_list(["",3,4,5,"",4,5])
  Out[240]: [0, 3, 4, 5, 5, 4, 5]"""
  new_list=[]
  for index,i in enumerate(a_list):
    if i: 
      new_list.append(i)
    else: continue
  return new_list
      
      
def make_nested_list(list_a,list_b):
  return [list(i) for i in zip(clean_none_from_list(list_a),clean_none_from_list(list_b))]

def main():
	pass


if __name__ == '__main__':
	main()

