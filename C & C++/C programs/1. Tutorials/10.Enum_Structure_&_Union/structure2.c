// -----Structure in C-----
#include <stdio.h>
#include <string.h>

struct book book_input(void);
struct book book_input_new(void);
void book_display(struct book);

struct book
{
    int bookid;
    char name[20];
    float price;
};

struct book book_input()
{
    struct book b;
    printf("Enter bookid, name and price:\n");
    scanf("%d", &b.bookid);
    // scanf can leave unwanted characters in the input buffer, which can cause issues when trying to read further input. The fflush function is used to clear the input buffer and discard any unprocessed input.
    fflush(stdin);
    gets(b.name);
    scanf("%f", &b.price);
    return (b);
}

struct book book_input_new()
{
    struct book b;
    char buffer[100];  // create a buffer to store input

    printf("Enter bookid, name and price:\n");
    scanf("%d", &b.bookid);

    // read and discard the rest of the line
    fgets(buffer, sizeof(buffer), stdin);

    // read the name of the book using fgets
    fgets(b.name, sizeof(b.name), stdin);

    // remove the newline character from the end of the string
    b.name[strlen(b.name) - 1] = '\0';

    scanf("%f", &b.price);
    return (b);
}

void book_display(struct book b)
{
    printf("\nbookid = %d, name = %s and price = %f", b.bookid, b.name, b.price);
}

void main()
{
    struct book b1;
    // b1 = book_input();
    b1 = book_input_new();
    book_display(b1);
}
