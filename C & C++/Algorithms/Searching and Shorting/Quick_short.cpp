// Quick Short Algorithm
#include <iostream>
using namespace std;

void swap(int *x, int *y)
{
    int t = *x;
    *x = *y;
    *y = t;
}

int partition(int arr[], int low, int high)
{
    int i = low - 1;
    for (int j = low; j < high; j++)
    {
        if (arr[j] < arr[high])
        {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return (i + 1);
}

void QuickShort(int arr[], int low, int high)
{
    if (low < high)
    {
        int pi = partition(arr, low, high);
        QuickShort(arr, low, pi - 1);
        QuickShort(arr, pi + 1, high);
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

    QuickShort(arr, 0, n - 1);
    printArray(arr, n);
    return 0;
}
