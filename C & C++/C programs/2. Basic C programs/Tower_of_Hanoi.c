// Program for 'Tower of Hanoi'
#include <stdio.h>
#include <conio.h>

void TOH(int n, char BEG, char AUX, char END)
{
    if (n >= 1)
    {
        TOH(n - 1, BEG, END, AUX);
        printf("%c to %c\n", BEG, END);
        TOH(n - 1, AUX, BEG, END);
    }
}

void main()
{
    int n;
    printf("\nEnter no. of disks in 'Tower of  Hanoi': ");
    scanf("%d", &n);
    TOH(n, 'A', 'B', 'C');
    getch();
}
