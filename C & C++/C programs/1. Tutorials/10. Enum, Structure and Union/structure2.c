// -----Structure in C-----
#include <stdio.h>

struct book input(void);
void book_display(struct book);

struct book
{
    int bookid;
    char name[20];
    float price;
};

struct book input()
{
    struct book b;
    printf("Enter bookid, name and price:\n");
    scanf("%d", &b.bookid);
    fflush(stdin);
    gets(b.name);
    scanf("%f", &b.price);
    return (b);
}

void display(struct book b)
{
    printf("\nbookid = %d, name = %s and price = %f", b.bookid, b.name, b.price);
}

void main()
{
    struct book b1;
    b1 = input();
    display(b1);
}
