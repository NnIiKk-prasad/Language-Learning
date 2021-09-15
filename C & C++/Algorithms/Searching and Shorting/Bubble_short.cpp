// Bubble Short Algorithm
#include <iostream>
using namespace std;

void swap(int *x, int *y)
{
    int t = *x;
    *x = *y;
    *y = t;
}

void BubbleShort(int arr[], int n)
{
    int round;
    for (round = 1; round < n; round++)
    {
        for (int i = 0; i < n - round; i++)
        {
            if (arr[i] > arr[i + 1])
                swap(arr[i], arr[i + 1]);
        }
    }
}

void printArray(int arr[], int n)
{
    cout << "\nShorted Array is: ";
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
}

int main()
{
    int n;
    cout << "Enter the length of array: ";
    cin >> n;

    int arr[n];
    cout << "\nEnter " << n << " integers:\n";
    for (int i = 0; i < n; i++)
        cin >> arr[i];

    BubbleShort(arr, n);
    printArray(arr, n);
    return 0;
}
