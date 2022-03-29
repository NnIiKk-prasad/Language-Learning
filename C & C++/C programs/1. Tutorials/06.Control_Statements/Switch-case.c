// -----Switch case in C-----
#include <stdio.h>
#include <stdlib.h>

void main()
{
    int choice, a, b;
    while (1)
    {
        printf("\n\n1. Addition\n2. Odd-Even\n3. Integers\n4. Exit\nEnter your choice: ");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            printf("\nEnter two numbers:\n");
            scanf("%d%d", &a, &b);
            printf("Sum of %d and %d is %d", a, b, a + b);
            break;
        case 2:
            printf("\nEnter a number: ");
            scanf("%d", &a);
            b = a % 2;
            if (b == 0)
                printf("Even");
            else
                printf("Odd");
            break;
        case 3:
            printf("\nEnter a number: ");
            scanf("%d", &a);
            for (b = 1; b <= a; b++)
            {
                printf("%d ", b);
            }
            break;
        case 4:
            exit(0);
        default:
            printf("\nInvalid Choice");
        }
    }
}
