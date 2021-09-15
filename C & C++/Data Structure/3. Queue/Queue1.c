// Queue implementation through array
#include <stdio.h>
#include <stdlib.h>

struct ArrayQueue
{
    int front, rear, capacity;
    int *array;
};

struct ArrayQueue *CreateQueue(int capacity)
{
    struct ArrayQueue *Q = (struct ArrayQueue *)malloc(sizeof(struct ArrayQueue));
    if (!Q)
        return (NULL);
    Q->capacity = capacity;
    Q->front = Q->rear = -1;
    Q->array = malloc(Q->capacity * sizeof(int));
    if (!Q->array)
        return (NULL);
    return (Q);
}

int isEmptyQueue(struct ArrayQueue *Q)
{
    return (Q->front == -1);
}

int isFullQueue(struct ArrayQueue *Q)
{
    return ((Q->rear + 1) % Q->capacity == Q->front);
}

int QueueSize(struct ArrayQueue *Q)
{
    return ((Q->capacity - Q->front + Q->rear + 1) % Q->capacity);
}

void enQueue(struct ArrayQueue *Q, int data)
{
    if (isFullQueue(Q))
    {
        printf("\nQueue Overflow");
    }
    else
    {
        Q->rear = (Q->rear + 1) % Q->capacity;
        Q->array[Q->rear] = data;
        if (Q->front == -1)
            Q->front = Q->rear;
        printf("Data inserted sucessfully!");
    }
}

int deQueue(struct ArrayQueue *Q)
{
    int data = -1;
    if (isEmptyQueue(Q))
    {
        printf("\nQueue is empty");
        return (data);
    }
    else
    {
        data = Q->array[Q->front];
        if (Q->front == Q->rear)
            Q->front = Q->rear = -1;
        else
            Q->front = (Q->front + 1) % Q->capacity;
        return (data);
    }
}

void deleteQueue(struct ArrayQueue *Q)
{
    if (Q)
    {
        if (Q->array)
        {
            free(Q->array);
        }
        free(Q);
    }
}

int menu()
{
    int ch;
    printf("\n\n1. Insert in Queue");
    printf("\n2. Delete in Queue");
    printf("\n3. Queue Size");
    printf("\n4. Is Full");
    printf("\n5. Exit");
    printf("\nEnter your choice: ");
    scanf("%d", &ch);
    return ch;
}

int main()
{
    int x, data;
    printf("\nEnter the size of Queue: ");
    scanf("%d", &x);
    struct ArrayQueue *que = CreateQueue(x);
    while (1)
    {
        switch (menu())
        {
        case 1:
            printf("\nEnter a value: ");
            scanf("%d", &data);
            enQueue(que, data);
            break;
        case 2:
            data = deQueue(que);
            if (data != -1)
                printf("\nDeleted value is %d ", data);
            break;
        case 3:
            printf("\nSize of Queue is %d", QueueSize(que));
            break;
        case 4:
            if (isFullQueue(que))
                printf("\nYes");
            else
                printf("\nNo");
            break;
        case 5:
            deleteQueue(que);
            exit(0);
        default:
            printf("\nInvalid choice");
        }
    }
    return 0;
}
