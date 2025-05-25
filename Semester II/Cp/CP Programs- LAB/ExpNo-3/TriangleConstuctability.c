#include<stdio.h>
int main()
{
	int a,b,c;
	printf("Enter 3 sides of triangle");
	scanf("%d%d%d",&a,&b,&c);
	if((a+b>c)&&(b+c>a)&&(a+c>b))
	{
		printf("\nTriangle can be drawn");
		if((a==b)&&(b==c)&&(a==c))
		{
			printf("\nEquilateral triangle");
		}
		else if((a!=b)&&(a!=c)&&(b!=c))
		{
			printf("\nScalene triangle");
		}
		else
		{
			printf("\nIsoscales triangle");
		}
	}
	else
	{
		printf("\nTriangle can not be drawn");
	}
	return 0;
}
