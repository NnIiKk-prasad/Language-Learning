// Linked List program in C
#include <stdio.h>
#include <stdlib.h>

struct node
{
    int info;
    struct node *link;
};

struct node *START = NULL;

struct node *createNode()
{
    struct node *n;
    n = (struct node *)malloc(sizeof(struct node));
    return (n);
}

void insertnode()
{
    struct node *temp, *t;
    temp = createNode();
    printf("\nEnter a number: ");
    scanf("%d", &temp->info);
    temp->link = NULL;
    if (START == NULL)
        START = temp;
    else
    {
        t = START;
        while (t->link != NULL)
            t = t->link;
        t->link = temp;
    }
    printf("\nSucessfully Added!");
}

void viewList()
{
    struct node *t;
    if (START == NULL)
        printf("\nList is empty");
    else
    {
        printf("\nList items are:\n");
        t = START;
        while (t != NULL)
        {
            printf("%d ", t->info);
            t = t->link;
        }
    }
}

void deleteNode()
{
    struct node *r;
    if (START == NULL)
        printf("\nList is empty");
    else
    {
        r = START;
        START = START->link;
        free(r);
        printf("\nSucessfully Deleted!");
    }
}

int menu()
{
    int ch;
    printf("\n\n1. Add value to list");
    printf("\n2. Delete first value");
    printf("\n3. View list");
    printf("\n4. Exit");
    printf("\nEnter your choice: ");
    scanf("%d", &ch);
    return (ch);
}

void main()
{
    while (1)
    {
        switch (menu())
        {
        case 1:
            insertnode();
            break;
        case 2:
            deleteNode();
            break;
        case 3:
            viewList();
            break;
        case 4:
            exit(0);
        default:
            printf("Invalid choice");
        }
    }
}
