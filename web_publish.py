#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2006-2008 Carlo Bifulco
# See LICENSE for details.






from google.appengine.ext import webapp
import os

from mako.template import Template as mako_template
from mako import exceptions
from mako.lookup import TemplateLookup





def template_path(template_name):
  return os.path.join(os.path.dirname(__file__),'templates',template_name+'.html')

def template_dir():
  return os.path.join(os.path.dirname(__file__),'templates')



def header():
  text='''
  
    <html>
    <head>
  <style media="screen,projection" type="text/css">
	
	/* BEGIN DEMO STYLE */
	*{margin:0;padding:0}
	body{padding:20px;background:white;background:white;color:#555;font:80%/140% 'helvetica neue',sans-serif;margin: 0 auto;}


	h1,h2{font:bold 80% 'helvetica neue',sans-serif;letter-spacing:3px;text-transform:uppercase;}
	li{padding-bottom:10px;}
	a{color:#348;text-decoration:none;outline:none;}
	ul{list-style-type: none;}
	a:hover{color:#67a;}
	
   big{
  -x-system-font:none;
  font-family:'helvetica neue',sans-serif;
  font-size:100%;
  font-size-adjust:none;
  font-stretch:normal;
  font-style:normal;
  font-variant:normal;
  font-weight:bold;
  letter-spacing:3px;
  line-height:normal;
  text-transform:uppercase;
  padding:2em;
  padding-bottom:2em;
  padding-top:2em}
  
  p{padding:1em;}
  
  b{font:bold 160% 'helvetica neue',sans-serif;letter-spacing:3px;text-transform:uppercase;}
  
  
  
	
	</style>




   
   
  '''
  return text
  
  
def footer():
  text='''
    <table >
	    <tbody>
	      <tr>
	        <td>
        	<a href='http://www.catb.org/hacker-emblem/'>
          <img src='http://www.catb.org/hacker-emblem/glider.png' alt='hacker emblem' /></a>
	        </td>
	      </tr>
	    </tbody>
	  </table>
	  </body>
</html>

  '''
  return text


    
class MakoTemplatedPage(webapp.RequestHandler):
  """Base class for templatized handlers."""
  mylookup = TemplateLookup(directories=["/sd"])  

  def write_template(self, **kwargs):
    """Write out the template with the same name as the class name."""
    path = template_path(self.__class__.__name__)
    template=mako_template(filename=path,lookup=TemplateLookup(directories=[os.path.dirname(__file__)]))
    text=header()
    try:
      text+= template.render(**kwargs)
      text+=footer()
    except:
      text+=exceptions.html_error_template().render()
    #print values
    self.response.out.write(text)





def main():
    pass


if __name__ == '__main__':
    main()

