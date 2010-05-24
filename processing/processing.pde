



class BarPainter{
  int[] data;
  PImage z, broken, broken_to_full,full_to_broken,full;

  float pad=20/10;
  float lenght=350;
    int h=480;
  int w=780;
    float step=h/7;
    float position;


  
  BarPainter(){
  
      broken=loadImage("broken.gif");
broken_to_full=loadImage("broken_to_full.gif");
full_to_broken=loadImage("full_to_broken.gif");
full=loadImage("full.gif");
data= new int[7];


     }
     
   void load(int a, int b, int c, int d, int e, int f){
       data[1]=a;
    data[2]=b;
    data[3]=c;
    data[4]=d;
    data[5]=e;
    data[6]=f;
   }
     
  void paint(float position){
    for (int i=1;i<7; i++){
        if (data[i]==0){z=broken;}
        if (data[i]==1){z=full;}
        if (data[i]==2){z=broken_to_full;}
        if (data[i]==3){z=full_to_broken;}
      image(z,position,height-((step+pad)*i));    
    
  }   
    }
  
  
  void test(){
  size(w, h);
  background(0);
  
  }
  
  
}


  
            

void drawAnotherLine() 
{
  // Create a new variable "a" local to this method
  int a = 185;
  // Draw a line using the local variable "a"
  line(a, 0, a, height);
}



 

void test(){

BarPainter b;
b=new BarPainter();
b.load(1,2,3,3,3,2);
b.test();
b.paint(20);}


void setup(){
size(640,480);
}





void draw(){
  BarPainter b;
b=new BarPainter();
b.load(1,2,3,3,3,2);
b.test();
b.paint(20);
  float m = millis();
  while (m<200){
     b.load(1,1,1,1,1,1);
    b.paint(20);
  println(m);}
  println("B loop");
  while (m<400){
  b.load(1,2,3,3,3,2);
  b.paint(20);
println(m);}
  }





