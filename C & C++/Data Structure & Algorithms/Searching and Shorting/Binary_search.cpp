// Binary Search Algorithm
#include <iostream>
using namespace std;

int bin_search(int A[], int left, int right, int k)
{
    if (left <= right)
    {
        int mid;
        mid = left + (right - left) / 2;
        if (A[mid] == k)
            return mid;
        else if (A[mid] > k)
            return bin_search(A, left, mid - 1, k);
        else
            return bin_search(A, mid + 1, right, k);
    }
    return -1;
}

int main()
{
    int t, N;

    cout << "Enter no. of test cases: ";
    cin >> t;

    cout << "\nEnter no. of elements of shorted array: ";
    cin >> N;

    int a[N];
    cout << "\nEnter " << N << " elements:" << endl;
    for (int i = 0; i < N; i++)
        cin >> a[i];

    int key;
    while (t--)
    {
        cout << "\nEnter the element to be found: ";
        cin >> key;
        int found = bin_search(a, 0, N - 1, key);
        if (found == -1)
            cout << "\nYour key is not in the array" << endl;
        else
            cout << "\nYour key is at the index = " << found << endl;
    }
    return 0;
}
