#include<stdio.h>
int main()
{
	int a,b,c,d,z;
	float e;
	printf("Enter 2 numbers=");
	scanf("%d%d",&a,&b);
	do
	{
	printf("\nMenu\n1-Addition\n2-Subtraction\n3-Multiplication\n4-Division\nEnter choice=");
	scanf("%d",&c);
	switch(c)
	{
		case 1:
			{
				d=a+b;
				printf("\nAddition=%d",d);
			}
			break;
		case 2:
			{
				d=a-b;
				printf("\nSubtraction=%d",d);
			}
			break;
		case 3:
			{
				d=a*b;
				printf("\nMultiplication=%d",d);
			}
			break;
		case 4:
			{
				e=(float)a/b;
				printf("\nDivision=%f",e);
			}
			break;
		default:
			{
				printf("\nInvalid choice");
			}
	}
	printf("\nPress 1 to continue...");
	scanf("%d",&z);
	}
	while(z==1);
	return 0;
}
