void setup() 
{
  size(200, 200);}
  
  void draw() {
    background(0);
   
    for (int i=0;i<100;i++){
      float r=random(20);
       stroke(255,10*r);
      strokeWeight(r);
      float offset=r*5.0;
      line(i+40,200,i+offset,0);
      
    }
  }
