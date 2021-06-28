#include<stdio.h>
int main()
{
    int i,j,n,k;

    printf("Enter the value of n\n");
    scanf("%d",&n);
    int arr[n][n];

    for(i=1;i<=n*n;i++)
    {
        j=(n-i%n+1+2*((i-1)/n))%n;    
        k=((n-1)/2+i-1-(i-1)/n)%n;  
        arr[n-j-1][n-k-1]=i;
    }

    for(j=0;j<n;j++)
    {
        for(k=0;k<n;k++)
        {
            printf("%d\t",arr[j][k]);
        }
        printf("\n");
    }
 
}