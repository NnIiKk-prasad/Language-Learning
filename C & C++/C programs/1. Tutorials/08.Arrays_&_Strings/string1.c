// -----Strings in C-----
#include <stdio.h>

void main()
{
    char s[10] = {'W', 'e', 'l', 'c', 'o', 'm', 'e', '\0'};
    int i;
    for (i = 0; s[i] != '\0'; i++)
        printf("%c", s[i]);

    char str[20];
    printf("\n\nEnter your name: ");
    // gets(&str[0]);
    gets(str);

    // printf("\nWelcome! ");
    // puts(str);
    printf("\nWelcome! %s", str);

    char str1[3][10];
    printf("\nEnter three strings:\n");
    for (i = 0; i <= 2; i++)
        gets(str1[i]); // or gets(&str1[i][0]);

    printf("\nYou entered:\n");
    for (i = 0; i <= 2; i++)
        printf("%s\n", str1[i]);
}
