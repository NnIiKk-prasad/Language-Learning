#include <iostream>
#include <array>
using namespace std;

int main()
{
    array<int, 5> data_array = {11, 22, 44, 66, 88};
    try
    {
        cout << data_array.at(6);
    }
    catch (out_of_range)
    {
        cout << "Index is out of range";
    }
}
