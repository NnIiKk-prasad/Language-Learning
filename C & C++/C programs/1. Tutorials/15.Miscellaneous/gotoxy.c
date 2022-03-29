#include <stdio.h>
#include <windows.h>

void gotoxy(int x, int y)
{
    COORD c;
    c.X = x;
    c.Y = y;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), c);
}

void main()
{
    int i;
    for (i = 10; i <= 20; i++)
    {
        gotoxy(40, i);

        printf("Nikhi Prasad");
    }
}
