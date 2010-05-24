#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by carlo on 2009-10-08.
Copyright (c) 2009 Carlo Bifulco. All rights reserved.
"""

import sys
import os
from pygooglechart import XYLineChart
from pygooglechart import Chart
from pygooglechart import SimpleLineChart
from pygooglechart import Axis


class SimpleLineTempChart:
  
  def __init__(self,data):
    x_size=900
    colours=['0000FF']
    y_size=200
    spacer=10
    y_range=[min(data)-spacer, max(data)+spacer]
    left_axis=range(y_range[0],y_range[1],5)
    self.chart=SimpleLineChart(x_size,y_size,y_range=y_range)
    self.chart.set_axis_labels(Axis.LEFT,left_axis)
    self.chart.set_colours(colours)
    self.chart.add_data(data)
    #self.chart.add_data(data)
  
  def get_url(self):
    return self.chart.get_url()
  



if __name__ == '__main__':
  data=[3,2,3,-4,5,12,-6,4,-6,2,3,5,4,3,4,5,6,4,3,2,3]
  for i in range(1):
    data.extend(range(1,10,1))
  t1=SimpleLineTempChart(data)
  #t2=TempChart(XYLineChart,data)
  print t1.get_url()
  #print t2.get_url()
  

  # cl=FinanceTester(email="carlobif@gmail.com", password="rinco69")
  # pf=cl.GetPortfolios()
  # data=[]
  # for i in pf.entry:
  #     PositionSizeGraph(i).show()
  #     GainGraph(i).show()
  #     PercentageGainGraph(i).show()
  # g=PercentageGainGraph(pf.entry[0])
  