// -----String related functions-----
#include <stdio.h>
#include <string.h>

void main()
{
    char str[20] = {'W', 'e', 'l', 'c', 'o', 'm', 'e', '\0'};
    printf("%d\n", strlen(str));

    printf("%s\n", strlwr(str));
    printf("%s\n", strupr(str));
    printf("%s\n", strrev(str));

    char str1[65], str2[98], str3[32] = {0};
    // The strcat function expects the destination string (the first argument) to have enough space to hold the concatenated string, and it appends the source string (the second argument) to the end of the destination string. If the destination string is not large enough to hold the concatenated string, it can lead to unpredictable results.
    strcpy(str1, "Harry");
    strcpy(str2, "Rohan");
    printf("\n%s %s", str1, str2);

    strcat(str3, str1);
    strcat(str3, str2);
    printf("\n%s", str3);

    printf("\n%d", strcmp(str1,str2));
}
