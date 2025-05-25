#include<stdio.h>
#include<math.h>
int main()
{
	float p,n,r,S,C;
	printf("Enter the principal amount, No. years and rate of interest:");
	scanf("%f%f%f",&p,&n,&r);
	S=(p*n*r)/100;
	C=p*pow((1+r/100),n)-p;
	printf("Simple interest is %f and Compound interest is %f",S,C);
	return 0;
}
