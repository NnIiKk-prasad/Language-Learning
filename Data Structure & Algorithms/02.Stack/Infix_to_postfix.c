// Conversion of Infix notation to Postfix notation using stack
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct arrayStack
{
    int top;
    int capacity;
    char *array;
};

struct arrayStack *createStack(int cap)
{
    struct arrayStack *stack;
    stack = (struct arrayStack *)malloc(sizeof(struct arrayStack));
    if (!stack)
        return NULL;
    stack->capacity = cap;
    stack->top = -1;
    stack->array = (char *)malloc(stack->capacity * sizeof(char));
    if (!stack->array)
        return NULL;
    return (stack);
}

int isEmpty(struct arrayStack *stack)
{
    return stack->top == -1;
}

void push(struct arrayStack *stack, char item)
{
    stack->array[++stack->top] = item;
}

char pop(struct arrayStack *stack)
{
    if (!isEmpty(stack))
        return stack->array[stack->top--];
    return '$';
}

char peek(struct arrayStack *stack)
{
    return stack->array[stack->top];
}

int isOperand(char ch)
{
    return (ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z');
}

int Prec(char ch)
{
    switch (ch)
    {
    case '+':
    case '-':
        return 1;
    case '*':
    case '/':
        return 2;
    case '^':
        return 3;
    default:
        return -1;
    }
}

int infixToPostfix(char exp[])
{
    char P[strlen(exp)];

    strncat(exp, ")", 1);

    struct arrayStack *stack = createStack(strlen(exp));
    if (!stack)
        return -1;
    push(stack, '(');

    int i, k;
    for (i = 0, k = -1; exp[i]; i++)
    {
        if (isOperand(exp[i]))
            P[++k] = exp[i];
        
        else if (exp[i] == '(')
            push(stack, exp[i]);
        
        else if (exp[i] == ')')
        {
            while (peek(stack) != '(')
            {
                P[++k] = pop(stack);
            }
            pop(stack);
        }

        else
        {
            while (Prec(exp[i]) <= Prec(peek(stack)))
                P[++k] = pop(stack);
            push(stack, exp[i]);
        }
    }
    // puts(P);
    printf("%s", P);
}

int main()
{
    char exp[] = "a+b*(c^d-e)^(f+g*h)-i";
    // char exp[] = "A+((B+C)+(D+E)*F)/G";
    infixToPostfix(exp);

    return 0;
}
