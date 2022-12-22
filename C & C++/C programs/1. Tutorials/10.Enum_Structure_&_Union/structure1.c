// -----Structure in C-----
#include <stdio.h>

struct date
{
    int d, m, y;
};

void main()
{
    struct date d1;
    printf("Enter a date in DD/MM/YYYY format:\n");
    scanf("%d/%d/%d", &d1.d, &d1.m, &d1.y);
    printf("\nDate: %d/%d/%d", d1.d, d1.m, d1.y);
}
