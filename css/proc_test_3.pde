var results=new Object(); 
Pimage bcg;
bcg=loadImage("background.gif");
broken=loadImage("broken.gif");
broken_to_full=loadImage("broken_to_full.gif");
full_to_broken=loadImage("full_to_broken.gif");
full=loadImage("full.gif");
Bars bars;

float pad=20/10;
float lenght=150
float step=480/7;
float h=480;
float w=640;
int counter=0;
int movedCounter=0;
int r;
int add_counter=0;
int sloop=1;



void setup() {
  size(w, h);
  background(bcg);
  bars= new Bars();

}


void draw(){
}


class Bars {

  
  Bars(){
  }
  

  
  void add(){
    if (counter<=1){
      background(bcg)};
      r=int(random(0,4));
      if (r==0){z=broken;}
      if (r==1){z=full;}
      if (r==2){z=broken_to_full;}
      if (r==3){z=full_to_broken;}
     // comunicator[counter]=r;
     
 
      image(z,width/2-(broken.width/2),height-((step+pad)*counter));
      results[counter]=r;

         }
         
    void reset(){
      counter=0;

      $("#inject_me").load("/jscript",results);
    }
}


class BarPainter{
  int i,a1,a2,a3,a4,a5,a6;
  int[] data;
  Barpainter(a1,a2,a3,a4,a4,a6){
    i=0;
    data[0]=a1;
    data[1]=a2;
    data[2]=a3;
    data[3]=a4;
    data[4]=a5;
    data[5]=a6;
     }
  void paint(){
    for (int i=0;i<6; i++){
        if (data[i]==0){z=broken;}
        if (data[i]==1){z=full;}
        if (data[i]==2){z=broken_to_full;}
        if (data[i]==3){z=full_to_broken;}   
    }
  }
  
  
}
      
      
void mousePressed() {



           bars.add();


               if (counter==6)
               {
  bars.reset();
   }
                counter+=1;


 
}


void mouseMoved() {
  if (counter==0){background(bcg);}
}

void mouseDragged(){
  float s=dist(mouseX,mouseY,pmouseX,pmouseY)+1;
  fill(255-(mouseX-pmouseX),255-(mouseY-pmouseY),mouseX-pmouseX+mouseY-pmouseY,50)
  noStroke();
  ellipse(mouseX,mouseY,s,s,1);
  
}

      
      
  
      
void rand(){
  random(1,4)
}
      
      

  



