// Stack implementation through array
#include <stdio.h>
#include <stdlib.h>

struct arrayStack
{
    int top;
    int capacity;
    int *array;
};

struct arrayStack *createStack(int cap)
{
    struct arrayStack *stack;
    stack = (struct arrayStack *)malloc(sizeof(struct arrayStack));
    stack->capacity = cap;
    stack->top = -1;
    stack->array = (int *)malloc(stack->capacity * sizeof(int));
    return (stack);
}

int isFull(struct arrayStack *stack)
{
    if (stack->top == stack->capacity - 1)
        return (1);
    else
        return (0);
}

int isEmpty(struct arrayStack *stack)
{
    if (stack->top == -1)
        return (1);
    else
        return (0);
}

void push(struct arrayStack *stack, int item)
{
    if (!isFull(stack))
    {
        stack->top++;
        stack->array[stack->top] = item;
        printf("\nItem pushed sucessfully!");
    }
    else
        printf("\nStack is full.");
}

void pop(struct arrayStack *stack)
{
    int item;
    if (!isEmpty(stack))
    {
        item = stack->array[stack->top];
        stack->top--;
        printf("\nPopped value is %d", item);
    }
    else
        printf("\nStack is empty");
}

void peek(struct arrayStack *stack)
{
    if (stack->top == -1)
    {
        printf("\nStack is empty.");
    }
    else
    {
        printf("\nTop item is %d", stack->array[stack->top]);
    }
}

int menu()
{
    int ch;
    printf("\n\n1. Push");
    printf("\n2. Pop");
    printf("\n3. Peek");
    printf("\n4. Exit");
    printf("\nEnter your choice: ");
    scanf("%d", &ch);
    return (ch);
}

int main()
{
    struct arrayStack *stack;
    stack = createStack(4);
    int item;
    while (1)
    {
        switch (menu())
        {
        case 1:
            printf("\nEnter a value: ");
            scanf("%d", &item);
            push(stack, item);
            break;
        case 2:
            pop(stack);
            break;
        case 3:
            peek(stack);
            break;
        case 4:
            exit(0);
        default:
            printf("\nInvalid choice");
        }
    }
    return 0;
}
