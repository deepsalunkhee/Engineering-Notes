 //Digital Differential Analyzer Line Drawing Algorithm
#include <graphics.h>
#include <stdio.h>
#include <math.h>
#include <conio.h>

ddaLine(int x1,int y1,int x2,int y2)
{
float x=x1,y=y1,dx,dy;
int step,i;
putpixel(x1,y1,WHITE);
if(abs(x2-x1)>=abs(y2-y1))
step=abs(x2-x1);
else
step=abs(y2-y1);
dx=(float)(x2-x1)/step;
dy=(float)(y2-y1)/step;
for(i=1;i<=step;i++)
{
x=x+dx;
y=y+dy;
putpixel((int) x,(int) y,WHITE);
}
}
main()
{
int x1,y1,x2,y2,gd,gm;
detectgraph(&gd,&gm);
initgraph(&gd, &gm, (char*)"");
printf("Enter the Co-ordinates of starting point of line: ");
scanf("%d %d",&x1,&y1);
printf("Enter the Co-ordinates of end point of line ");
scanf("%d %d",&x2,&y2);
ddaLine(x1,y1,x2,y2);
getch();
closegraph();
}

