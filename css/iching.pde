




var results=new Object(); 

     noLoop();
Pimage bcg;
  bcg=loadImage("background.gif");

broken=loadImage("broken.gif");
broken_to_full=loadImage("broken_to_full.gif");
full_to_broken=loadImage("full_to_broken.gif");
full=loadImage("full.gif");

 float pad=broken.height/10;
 float lenght=broken.width;
 float step=bcg.height/7;
 int counter=0;
 int movedCounter=0;
 int r;
 int add_counter=0;
 
 int[] y = new int[bcg.height]
 int[] x = new int[bcg.width]
 strokeWeight(51);
 stroke(0)
 
 line(0,0,width,0);
 line(0,0,0,height);
 line(width,height,width,0);
 line(width,height,0,height);


void setup() {

  

    size(bcg.width, bcg.height);
    background(bcg);

     background(bcg);
      image(bcg, 0, 0);



  


   
}

void draw() {
  background(0);
}

void run() {


         
 add();

  
     if (counter==6)
     {
    
       counter=0;
  
      $("#inject_me").load("/jscript",results);}
      counter+=1;
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
        
      
      
      void mousePressed() {
        run();
        float s=dist(mouseX,mouseY,pmouseX,pmouseY)+1;
        fill(255-(mouseX-pmouseX),255-(mouseY-pmouseY),mouseX-pmouseX+mouseY-pmouseY,20)
        noStroke();
        ellipse(mouseX,mouseY,s,s);
      }

      
      
      add(full);
      
void rand(){
  random(1,4)
}
      
      

  




