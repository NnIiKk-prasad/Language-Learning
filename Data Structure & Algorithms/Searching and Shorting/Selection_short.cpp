// Selection Short Algorithm
#include <iostream>
using namespace std;

void swap(int *x, int *y)
{
    int t = *x;
    *x = *y;
    *y = t;
}

void SelectionShort(int arr[], int n)
{
    int min_idx;
    for (int i = 0; i < n; i++)
    {
        min_idx = i;
        for (int j = i + 1; j < n; j++)
        {
            if (arr[j] < arr[min_idx])
                min_idx = j;
        }
        swap(arr[i], arr[min_idx]);
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

    SelectionShort(arr, n);
    printArray(arr, n);
    return 0;
}
