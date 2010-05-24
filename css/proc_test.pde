

int image_width=147;
int image_height=39;
int hstart;
int wstart;
int counter;


void setup() 
{
  size(800, 100);  
    wstart=width/image_width;
  hstart=(height-2*(height/image_height));
 //img=loadImage("test.png");
    //img1=loadImage("test.jpg");
  // back_ground= loadImage("background.png");
  // broken_bar= loadImage("brokenBar.png");
  // broken_to_full= loadImage("brokenToFull.png");
  // full_bar= loadImage("fullBar.png");
   //full_to_broken= loadImage("fullToBroken.png");
     //background(0);
     fill(0,0,0);
       //image(img, 0, 0);
       //image(img, 0, 0);
       smooth();
      // image(img,mouseX-img.width/2, mouseY);
diagonal= new Blade(100,100);
  background(0);
  counter=0;
  strokeWeight(2);
}

void draw() 
{
  //image(img,mouseX-img.width/2, mouseY);
diagonal.grow();
if (counter<100){
  background(0 );
  counter+=1;}
  
  // noStroke();
  //  ellipse(66,46,80,80);
  //  color c=get(mouseX,mouseY);

  //  float r=red(c);
  //  stroke(255-r);
  //  line(0,0,480,480);
  //  line(40,40,480,480);
  //  line(40,40,300,233);
  // 
  if (mousePressed==true){
  float s=dist(mouseX,mouseY,pmouseX,pmouseY)+1;
  fill(255-(mouseX-pmouseX),255-(mouseY-pmouseY),mouseX-pmouseX+mouseY-pmouseY,20)
  noStroke();
  ellipse(mouseX,mouseY,s,s);}
     //image(img, 0, 0);
  //stroke(255);
  //point(mouseX,mouseY);}
// line(mouseX,0, mouseX,height);
// line(0,mouseY, width,mouseY);
//   line(mouseX,mouseY,pmouseX,pmouseY);
   // filter(BLUR,3);
  //filter(BLUR,3);
  //image(full_bar,wstart,hstart);
}

void mouseMoved(){
  diagonal.seed(mouseX,mouseY);
}


class Blade{
  float x,y;
  float x1,y1,x2,y2;
  
  Blade(int xpos, int ypos){
    x=xpos;
    y=ypos;
  }
  
  void seed(int xpos, int ypos){
    x=xpos;
    y=ypos;
    x1=xpos;
    y1=ypos;
    x2=xpos;
    y2=ypos;
  }
  
  void grow(){
      //float x1,y1,x2,y2;
     if (mousePressed==true){
       x1=random(-5,width);
       y1=random(-5,height);
       x2=random(-10,width);
       x2=random(-10,height);
       noStroke()
       fill(random(0,255),random(0,255),random(0,255),0);
    
       rect(x1,y1,x2,3);
          stroke(random(0,255),random(0,255),random(0,255),25);
    x+=0.5;
   y-=1.0;
    line(x,y,x1,y1);
    }
  }
}