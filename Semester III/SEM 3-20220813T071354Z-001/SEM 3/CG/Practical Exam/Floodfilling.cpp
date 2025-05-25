// Flood Filling Algorithm
#include<stdio.h>
#include<graphics.h>
flood_fill(int x,int y,int new_col,int old_col)
{
 if(getpixel(x,y)==old_col)
 {
 putpixel(x,y,new_col);
 flood_fill(x+1,y,new_col,old_col);
 flood_fill(x-1,y,new_col,old_col);
 flood_fill(x,y+1,new_col,old_col);
 flood_fill(x,y-1,new_col,old_col);
 }
}
main()
{
int gdriver,gmode;
detectgraph(&gdriver,&gmode);
initgraph(&gdriver,&gmode,(char*)"");
circle(200,150,35);
circle(100,150,35);
arc(150,150,45,135,35);
arc(150,150,225,315,35);
arc(150,115,0,180,50);
arc(150,185,180,360,50);
flood_fill(200,150,GREEN,getpixel(200,150));
flood_fill(150,150,YELLOW,getpixel(150,150));
flood_fill(80,150,BROWN,getpixel(80,150));
flood_fill(150,100,RED,getpixel(150,100));
flood_fill(150,200,BLUE,getpixel(150,200));
getch();
closegraph();
}

