#include <stdio.h>
void main()
{
    int andis = 4;
    int num1 = 0;
    int num2 = 1;
    int sum = 0;
    for (int i = 1; i <= 5; i++)
    {
        for (int z = andis; z >= 1; z--)
        {
            printf("\t");            
        }
        andis -=1;
        for (int j = 1; j <= i; j++)
        {
         if (i == 1)
         {
            printf("%d\t",num1);
         }
         else if (i == 2)
         {
            printf("%d\t\t",num2);
            num1 =1;
            num2 = 1;
        
         }
         else
         {
            sum = num1 + num2;
            num1 = num2;
            num2 = sum;
            printf("%d\t\t",sum);
         }
         
         
        }
        
        printf("\n");
        
    }
    
}