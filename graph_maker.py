#!/usr/bin/env python
# encoding: utf-8
"""
graph_maker.py

Created by carlo bifulco on 2009-07-14.
Copyright (c) 2009 CBB inc.. All rights reserved.
"""

import sys
import os
from mako.template import Template as mako_template
from mako import exceptions
import random

def random_hex_color():
  a=""
  for i in range(6):
    a+=random.choice(["A","B","C","D","E","F"])
  return a

def hex_list(n):
  l=["000000", "0000FF","DEB887","A9A9A9","8B008B","FFD700","FF0000", "00FF00", 
  "FFFF00","00FFFF","FF00FF,""FFFFF0","7CFC00","B8860B","BDB76B"]
  for i in range(len(l),n):
    a=random_hex_color()
    if a not in l:
      l.append(a)
  return l
  
colors=["000000", "0000FF","DEB887","A9A9A9","8B008B","FFD700","FFFFF0","7CFC00","B8860B","BDB76B"]
    


class AbsGraph:
  def __init__(self,span_id="test_id",graph_type="bhs",x=500,y=600,data=[],axis_labels=[],legend=[]):
    self.span_id=span_id
    self.graph_type=graph_type
    self.x=x
    self.y=y
    self.data=data
    self.axis_labels=axis_labels
    self.legend=legend
    self.colors=hex_list(len(legend))
    self.template= ""
    
          
  def spit(self):
    try:
      return mako_template(self.template).render(span_id=self.span_id,
                                                graph_type=self.graph_type,
                                                x=self.x,
                                                y=self.y,
                                                data=self.data,
                                                axis_labels=self.axis_labels,
                                                legend=self.legend,
                                                colors=self.colors)
    except:
      return exceptions.html_error_template().render()




class NestedGraph(AbsGraph):
  def __init__(self,span_id="test_id",graph_type="bhs",x=500,y=600,data=[],axis_labels=[],legend=[]):
    AbsGraph.__init__(self,span_id=span_id,graph_type=graph_type,x=x,y=y,data=data,axis_labels=axis_labels,legend=legend)
    tag= """<span id="${span_id}">${span_id}</span>"""
    
    self.template= """<span id="${span_id}">${span_id}</span>
            <script type="text/javascript">
            var api = new jGCharts.Api(); 
            jQuery('<img>').attr('src', api.make(
            {
              colors : ${colors},
              chbg          : 'FFFFFF', 
              size : '${x}x${y}',
              //bar 
              bar_width   : ${(y-(8*len(data)))/len(data)}, 
              bar_spacing : 0, 
              
              data :[
              %for index,i in enumerate(data):
              [
              %for n,z in enumerate(i):
              ${int(z)}
              %if n!=len(i)-1:
              ,
              %endif
              %endfor
              ]
              %if index!=len(data)-1:
              ,
              %endif
              %endfor
              ],
              type      : "${graph_type}", 
              axis_labels :[
              %for n,i in enumerate(axis_labels):
              '${str(i)}'
              %if n!=len(axis_labels)-1:
              ,
              %endif
              %endfor
              ],
              legend :[
              %for index,i in enumerate(legend):
              '${str(i)}'
              %if index!=len(legend)-1:
              ,
              %endif
              %endfor
              ]
              }
            )).appendTo("#${span_id}")
            </script>
            """
            
class LinearGraph(AbsGraph):
  def __init__(self,span_id="test_id",graph_type="bhs",x=500,y=600,data=[],axis_labels=[],legend=[]):
    AbsGraph.__init__(self,span_id=span_id,graph_type=graph_type,x=x,y=y,data=data,axis_labels=axis_labels,legend=legend)
    tag= """<span id="${span_id}">${span_id}</span>"""

    self.template= """<span id="${span_id}">${span_id}</span>
            <script type="text/javascript">
            var api = new jGCharts.Api(); 
            jQuery('<img>').attr('src', api.make(
            {
              colors : ${colors},
              chbg          : 'FFFFFF', 
              size : '${x}x${y}',
              //bar 
              bar_width   : ${(y-(8*len(data)))/len(data)}, 
              bar_spacing : 0, 

              data :[
              %for index,i in enumerate(data):
              ${int(i)}
              %if index!=len(data)-1:
              ,
              %endif
              %endfor
              ],
              type      : "${graph_type}", 
              axis_labels :[
              %for n,i in enumerate(axis_labels):
              '${str(i)}'
              %if n!=len(axis_labels)-1:
              ,
              %endif
              %endfor
              ],
              legend :[
              %for index,i in enumerate(legend):
              '${str(i)}'
              %if index!=len(legend)-1:
              ,
              %endif
              %endfor
              ]
              }
            )).appendTo("#${span_id}")
            </script>
            """
          
  def spit(self):
    try:
      return mako_template(self.template).render(span_id=self.span_id,
                                                graph_type=self.graph_type,
                                                x=self.x,
                                                y=self.y,
                                                data=self.data,
                                                axis_labels=self.axis_labels,
                                                legend=self.legend,
                                                colors=self.colors)
    except:
      return exceptions.html_error_template().render()


def main():
	pass


if __name__ == '__main__':
	main()

