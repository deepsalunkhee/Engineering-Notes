#include<stdio.h>
#include<math.h>
int main()
{
	int a,b,c;
	float d,r1,r2,x,y;
	printf("Enter coefficients of quadratic equation=");
	scanf("%d%d%d",&a,&b,&c);
	d=b*b-4*a*c;
	if(d>0)
	{
		printf("\nReal roots");
		r1=(-b+sqrt(d))/(2*a);
		r2=(-b-sqrt(d))/(2*a);
		printf("\nRoot1=%f and Root2=%f",r1,r2);
	}
	else if(d<0)
	{
		printf("\nComplex Roots");
		x=-b/(2*a);
		y=sqrt(-d)/(2*a);
		printf("\nRoot1=%f+i%f",x,y);
		printf("\nRoot2=%f-i%f",x,y);
	}
	else
	{
		printf("\nEqual roots");
		r1=r2=-b/(2*a);
		printf("\nRoot1=Root2=%f",r1);
	}
	return 0;
}
