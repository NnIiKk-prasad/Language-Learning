#include <iostream>
#include <array>
using namespace std;

int main()
{
    array<int, 8> data_array = {11, 22, 44, 66, 88};
    cout << data_array.at(2) << endl;
    cout << data_array.front() << endl;
    cout << data_array.back() << endl;
    cout << data_array.size() << endl;

    array<int, 5> data_array1 = {11, 22, 44, 66, 88};
    array<int, 5> data_array2 = {1, 2, 4, 6, 8};
    data_array1.swap(data_array2);
    for (int i = 0; i < 4; i++)
    {
        cout << data_array1[i] << " ";
    }
    cout << endl;
    for (int i = 0; i < 4; i++)
    {
        cout << data_array2[i] << " ";
    }
    cout << endl;

    array<int, 5> data_array3;
    data_array3.fill(10);
    for (int i = 0; i < 4; i++)
    {
        cout << data_array3[i] << " ";
    }
    cout << endl;
}
