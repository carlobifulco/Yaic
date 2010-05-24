from pyprocessing import *
  
    
def setup():
  global img
  smooth()
  size(1000,1000)
  img = loadImage("./images/test.png")
  tint(0, 153, 204, 126); 
  
  
def draw():


  for y in range(height):
    image(img,0,0)
    line(0,y,width,y)
      
  for i in range(10):
    line(i*5+5,20,i*5+50,80)
  #print width, height
    
    
##img = loadImage("./images/test.png")
# black = color(0, 0, 0);
# img.set(30, 20, black); 
# img.set(85, 20, black); 
# img.set(85, 75, black); 
# img.set(30, 75, black); 
# image(img, 0, 0);

run()



