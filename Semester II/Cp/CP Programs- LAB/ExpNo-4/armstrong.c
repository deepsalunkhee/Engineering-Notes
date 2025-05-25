#include<stdio.h>
#include<math.h>
int main()
{
	int n,d,c1,c2,sum=0,count=0;
	printf("Enter number=");
	scanf("%d",&n);
	c2=c1=n;
	while(c1!=0)
	{
		c1=c1/10;
		count++;
	}
	while(c2!=0)
	{
		d=c2%10;
		sum=sum+pow(d,count);
		c2=c2/10;
	}
	if(n==sum)
	{
		printf("Armstrong number");
	}
	else
	{
		printf("Not armstrong number");
	}
	return 0;
}
	
	
	
	
	
