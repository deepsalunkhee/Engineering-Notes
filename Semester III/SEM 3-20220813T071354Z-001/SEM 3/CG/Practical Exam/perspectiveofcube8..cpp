//Study and implement perspective projection of a cube
#include<stdio.h>
#include<math.h>
#include<graphics.h>
main()
{
int x1,y1,x2,y2,gd,gm;
int ymax,a[4][8];
float par[4][4],b[4][8];
int i,j,k,m,n,p;
int xp, yp, zp, x, y, z;
a[0][0] = 100; a[1][0] = 100; a[2][0] = -100;
a[0][1] = 200; a[1][1] = 100; a[2][1] = -100;
a[0][2] = 200; a[1][2] = 200; a[2][2] = -100;
a[0][3] = 100; a[1][3] = 200; a[2][3] = -100;
a[0][4] = 100; a[1][4] = 100; a[2][4] = -200;
a[0][5] = 200; a[1][5] = 100; a[2][5] = -200;
a[0][6] = 200; a[1][6] = 200; a[2][6] = -200;
a[0][7] = 100; a[1][7] = 200; a[2][7] = -200;
detectgraph(&gd,&gm);
initgraph(&gd,&gm, (char*)"");

ymax = getmaxy();
xp = 300; yp = 320; zp = 100;
for(j=0; j<8; j++)
{
x = a[0][j]; y = a[1][j]; z = a[2][j];
b[0][j] = xp - ( (float)( x - xp )/(z - zp)) * (zp);
b[1][j] = yp - ( (float)( y - yp )/(z - zp)) * (zp);
}
/*- front plane display -*/
for(j=0;j<3;j++)
{
x1=(int) b[0][j]; y1=(int) b[1][j];
x2=(int) b[0][j+1]; y2=(int) b[1][j+1];
line( x1,ymax-y1,x2,ymax-y2);
}
x1=(int) b[0][3]; y1=(int) b[1][3];
x2=(int) b[0][0]; y2=(int) b[1][0];
line( x1, ymax-y1, x2, ymax-y2);
/*- back plane display -*/
setcolor(11);
for(j=4;j<7;j++)
{
x1=(int) b[0][j]; y1=(int) b[1][j];
x2=(int) b[0][j+1]; y2=(int) b[1][j+1];

line( x1, ymax-y1, x2, ymax-y2);
}
x1=(int) b[0][7]; y1=(int) b[1][7];
x2=(int) b[0][4]; y2=(int) b[1][4];
line( x1, ymax-y1, x2, ymax-y2);
setcolor(7);
for(i=0;i<4;i++)
{
x1=(int) b[0][i]; y1=(int) b[1][i];
x2=(int) b[0][4+i]; y2=(int) b[1][4+i];
line( x1, ymax-y1, x2, ymax-y2);
}
getch();
}
