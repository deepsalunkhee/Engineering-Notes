#include<stdio.h>
#include<conio.h>
#include<graphics.h>
int main()
{
	int x,y,x1,y1,x2,y2,dx,dy,p,i;
	int gd=DETECT,gm;
	initgraph(&gd,&gm,(char*)"");
	printf("Enter co-ordinates of first point :");
	scanf("%d%d",&x1,&y1);
	printf("Enter co-ordinates of second point :");
	scanf("%d%d",&x2,&y2);
	dx=x2-x1;
	dy=y2-y1;
	x=x1;
	y=y1;
	i=0;
	while(i<=dx)
	{
		if(p<0)
		{
			putpixel(x,y,WHITE);
			x=x+1;
			p=p+2*dy;
		}
		else
		{
			putpixel(x,y,WHITE);
			x=x+1;
			y=y+1;
			p=p+2*dy-2*dx;
		}
	i++;
	delay(500);	
	}
	closegraph();
	return 0;
}
