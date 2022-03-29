// Stack implementation using linked list
#include <stdio.h>
#include <stdlib.h>

struct node
{
    int info;
    struct node *next;
};

struct node *stack = NULL;

struct node *create_node()
{
    struct node *n;
    n = (struct node *)malloc(sizeof(struct node));
    return (n);
}

void push(int item)
{
    struct node *n;
    n = create_node();
    if (n != NULL)
    {
        if (stack == NULL)
        {
            n->info = item;
            n->next = NULL;
            stack = n;
        }
        else
        {
            n->info = item;
            n->next = stack;
            stack = n;
        }
        printf("\nItem pushed sucessfully!");
    }
}

void peek()
{
    if (stack == NULL)
    {
        printf("\nStack is empty");
    }
    else
    {
        printf("\nTop item is %d", stack->info);
    }
}

void pop()
{
    int item;
    struct node *r;
    if (stack == NULL)
    {
        printf("\nStack is underflow");
    }
    else
    {
        item = stack->info;
        r = stack;
        stack = r->next;
        free(r);
        printf("\nPopped value is %d", item);
    }
}

void remove_stack()
{
    struct node *r;
    if (stack == NULL)
    {
        printf("\nStack is already empty");
    }
    else
    {
        do
        {
            r = stack;
            stack = stack->next;
            free(r);
        } while (stack != NULL);
        printf("\nStack is removed");
    }
}

int menu()
{
    int ch;
    printf("\n\n1. Push");
    printf("\n2. Peek");
    printf("\n3. Pop");
    printf("\n4. Remove Stack");
    printf("\n5. Exit");
    printf("\nEnter your choice: ");
    scanf("%d", &ch);
    return ch;
}

int main()
{
    int item;
    while (1)
    {
        switch (menu())
        {
        case 1:
            printf("\nEnter a value: ");
            scanf("%d", &item);
            push(item);
            break;
        case 2:
            peek();
            break;
        case 3:
            pop();
            break;
        case 4:
            remove_stack();
            break;
        case 5:
            exit(0);
        default:
            printf("\nInvalid choice");
        }
    }
    return 0;
}
