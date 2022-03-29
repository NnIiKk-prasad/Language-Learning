// -----If - Else ladder-----
#include <stdio.h>

void main()
{
    // Program to check your grade
    int x;
    printf("Enter your percentage: ");
    scanf("%d", &x);
    if (x > 90)
        printf("Grade A");
    else if (x > 80)
        printf("Grade B");
    else if (x > 70)
        printf("Grade C");
    else
        printf("Grade D");
}
