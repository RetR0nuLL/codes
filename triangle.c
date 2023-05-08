#include <stdio.h>
int main()
{
    int andis = 4;
    int andis2 =0;
    int x=0;
    for (int i = 1; i <= 5; i++)
    {
        for (int z = andis; z >= 1; z--)
        {
            printf("\t");            
        }
        andis -=1;
        for (int j = 1; j <= i; j++)
        {
            printf("%d\t",j);
            andis2 = j - 1;
        }
        for (int k = 1; k < i; k++)
        {
            printf("%d\t",andis2);
            andis2 -= 1;
            x += 1;
        }
        andis2 += x;
        x = 0;
        
        printf("\n");
        
    }
    return 0;
}