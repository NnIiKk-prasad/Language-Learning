// Queue implementation through array
#include <iostream>
using namespace std;

class Queue
{
    int Front, Rear, Capacity;
    int *Array;

public:
    Queue(int Capacity);
    int isEmpty();
    int isFull();
    int Size();
    void enQueue(int data);
    int deQueue();
    void deleteQueue();
};

Queue::Queue(int Cap)
{
    Capacity = Cap;
    Front = Rear = -1;
    Array = (int *)malloc(Capacity * sizeof(int));
}

int Queue::isEmpty()
{
    return (Front == -1);
}

int Queue::isFull()
{
    return ((Rear + 1) % Capacity == Front);
}

int Queue::Size()
{
    return ((Capacity - Front + Rear + 1) % Capacity);
}

void Queue::enQueue(int data)
{
    if (this->isFull())
    {
        cout << "Overflow";
    }
    else
    {
        Rear = (Rear + 1) % Capacity;
        Array[Rear] = data;
        if (Front == -1)
            Front = Rear;
    }
}

int Queue::deQueue()
{
    int data = -1;
    if (this->isEmpty())
    {
        cout << "Queue is empty";
        return (data);
    }
    else
    {
        data = Array[Front];
        if (Front == Rear)
            Front = Rear = -1;
        else
            Front = (Front + 1) % Capacity;
        return (data);
    }
}

void Queue::deleteQueue()
{
    free(Array);
}

int main()
{
    int x, ch, data;
    cout << "Enter the size of Queue ";
    cin >> x;
    Queue Q(x);
    while (1)
    {
        cout << "\n\n1. Insert in Queue";
        cout << "\n2. Delete in Queue";
        cout << "\n3. Queue Size";
        cout << "\n4. Is Full";
        cout << "\n5. Exit";
        cout << "\nEnter your choice ";
        cin >> ch;
        switch (ch)
        {
        case 1:
            cout << "Enter a value ";
            cin >> data;
            Q.enQueue(data);
            break;
        case 2:
            data = Q.deQueue();
            if (data != -1)
                cout << "Deleted value is " << data;
            break;
        case 3:
            cout << "Size of Queue is " << Q.Size();
            break;
        case 4:
            if (Q.isFull())
                cout << "Yes";
            else
                cout << "No";
            break;
        case 5:
            Q.deleteQueue();
            exit(0);
        default:
            cout << "Invalid choice";
        }
    }
    return 0;
}
