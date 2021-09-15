// Program to check wether a number is prime or not
#include <stdio.h>

void main()
{
    int n, i, flag;
    printf("Enter a number:\n");
    scanf("%d", &n);
    if (n > 0)
    {
        flag = 0;
        for (i = 2; i <= n / 2; i++)
            if (n % i == 0)
            {
                flag = 1;
                break;
            }
        if (flag == 0)
            printf("%d is a prime number", n);
        else
            printf("%d is not a prime number", n);
    }
    else
        printf("Your number is not valid");
}
