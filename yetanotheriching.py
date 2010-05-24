#!/usr/bin/env python
#
#(c) Copyright 2009 carlo bifulco. All Rights Reserved. 


if __name__ != '__main__':
  try:
    import gae_test
  except:
    pass

import wsgiref.handlers
from google.appengine.ext import webapp
import web_publish
import cgi
from google.appengine.api import users
import datetime
import graph_maker
from utilities import now_pacific_day
import graph
import utilities
import gdata.finance.service
from mako.template import Template as mako_template
from mako import exceptions
from mako.lookup import TemplateLookup
import pywapi
import web_data
from graph import SimpleLineTempChart
import simplejson as json


iChingKeys={
    "111111":(1,"Ch'ien","The Creative"),
    "111100":(34,"Ta Chuang","The Power of the Great"),
    "111010":(5,"Hsu","Waiting"),
    "111001":(26,"Ta Ch'u","The Taming Power of the Great"),
    "111000":(11,"T'ai","Peace"),
    "111011":(9,"Hsiao Ch'u","The Taming Power of the Small"),
    "111101":(14,"Ta Yu", "Possession in Great Measure"),
    "111110":(43,"Kuai", "Break-through (Resoluteness)"),
    "100111":(25,"Wu Wang","Innocence (The Unexpected)"),
    "100100":(51,"Chen","The Arousing (Shock, Thunder)"),
    "100010":(3,"Chun","Difficulty at the Beginning"),
    "100001":(27,"I","Corners of the Mouth (Providing Nourishment)"),
    "100000":(24,"Fu","Return (The Turning Point)"),
    "100011":(42,"I","Increase"),
    "100101":(21,"Shih Ho","Biting Through"),
    "100110":(17,"Sui","Following"),
    "010111":(6,"Sung","Conflict"),
    "010100":(40,"Hsieh","Deliverance"),
    "010010":(29,"K'an","The Abysmal (Water)"),
    "010001":(4,"Meng","Youthful Folly"),
    "010000":(7,"Shih","The Army"),
    "010011":(59,"Huan","Dispersion (Dissolution)"),
    "010101":(64,"Wei Chi", "Before Completion"),
    "010110":(47,"K'un","Oppression (Exhaustion)"),
    "001111":(33,"Tun", "Retreat"),
    "001100":(62,"Hsiao Kuo", "Preponderance of the Small"),
    "001010":(39,"Chien", "Obstruction"),
    "001001":(52,"Ken", "Keeping Still (Mountain)"),
    "001000":(15,"Ch'ien","Modesty"),
    "001011":(53,"Chien","Development"),
    "001101":(56,"Lu","The Wanderer"),
    "001110":(31,"Hsien","Influence"),
    "000111":(12,"P'i","Standstill (Stagnation)"),
    "000100":(16,"Yu","Enthusiasm"),
    "000010":(8,"Pi","Holding Together (Union)"),
    "000001":(23,"Po","Splitting Apart"),
    "000000":(2,"K'un","The Receptive"),
    "000011":(20,"Kuan","Contemplation (View)"),
    "000101":(35,"Chin","Progress"),
    "000110":(45,"Ts'ui","Gathering Together (Massing)"),
    "011111":(44,"Kou", "Coming to Meet"),
    "011100":(32,"Heng", "Duration"),
    "011010":(48,"Ching", "The Well"),
    "011001":(18,"Ku", "Work on what has been spoiled (Decay)"),
    "011000":(46,"Sheng","Pushing Upward"),
    "011011":(57,"Sun","The Gentle (The Penetrating, Wind)"),
    "011101":(50,"Ting","The Caldron"),
    "011110":(28,"Ta Kuo", "Preponderance of the Great"),
    "101111":(13,"T'ung Jen","Fellowship with Men"),
    "101100":(55,"Feng","Abundance (Fullness)"),
    "101010":(63,"Chi Chi","After Completion"),
    "101001":(22,"Pi", "Grace"),
    "101000":(36,"Ming I", "Darkening of the Light"),
    "101011":(37,"Chia Jen","The Family (The Clan)"),
    "101101":(30,"Li","The Clinging (Fire)"),
    "101110":(49,"Ko","Revolution (Molting)"),
    "110111":(10,"Lu","Treading (Conduct)"),
    "110100":(54,"Kuei Mei","The Marrying Maiden"),
    "110010":(60,"Chieh","Limitation"),
    "110001":(41,"Sun", "Decrease"),
    "110000":(19,"Lin","Approach"),
    "110011":(61,"Chung Fu","Inner Truth"),
    "110101":(38,"K'uei","Opposition"),
    "110110":(58,"Tui","The Joyous (Lake)")
    }

    
    

    
    



def get_host_name():
  port = os.environ['SERVER_PORT']
  if port and port != '80':
    HOST_NAME = '%s:%s' % (os.environ['SERVER_NAME'], port)
  else:
    HOST_NAME = os.environ['SERVER_NAME']
  return HOST_NAME
  



class MainHandler(web_publish.MakoTemplatedPage):
  def get(self):
    self.write_template()
 



class JscriptTester(web_publish.MakoTemplatedPage):
  def post(self):
    results=[]
    results_positions=[1,2,3,4,5,6]
    for i in results_positions:
      results.append(self.request.get(str(i)))
    results="".join(results)
    currentResult=results.replace("2","0").replace("3","1")
    futureResult=self.answer.replace("3","0").replace("2","1")
    iChingCurrentResult=str(iChingKeys[currentResult][0])
    iChingFutureResult=str(iChingKeys[futureResult][0])
    template_path=web_publish.template_path(iChingCurrentResult)
    #self.response.out.write("SDSSDS")
    self.response.out.write(mako_template(filename=template_path).render())
  




def main():
  application = webapp.WSGIApplication([('/', MainHandler),
                                        ("/jscript",JscriptTester),],
                                       debug=True)
                                       
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()

