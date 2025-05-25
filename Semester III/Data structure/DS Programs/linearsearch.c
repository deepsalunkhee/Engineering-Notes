#include<stdio.h>
int linearsearch(int a[],int n,int x)
{
	int i;
	for(i=0;i<n;i++)
	{
		if(x==a[i])
		{
			return 1;
		}
	}
	return 0;
}

int main()
{
	int a[100],n,i,x,z;
	printf("\nEnter bumber of elements=");
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		printf("\nEnter element=");
		scanf("%d",&a[i]);
	}
	printf("\nEnter element to be searched=");
	scanf("%d",&x);
	z=linearsearch(a,n,x);
	if(z==1)
	{
		printf("\nElement is present...");
	}
	else
	{
		printf("\nElement is not present...");
	}
	return 0;
}
