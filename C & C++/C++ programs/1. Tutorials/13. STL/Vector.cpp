#include <iostream>
#include <vector>
using namespace std;

int main()
{
    vector<int> v1{10, 20, 30, 40, 50};
    cout << "Value at index 3 is " << v1.at(3) << endl;
    cout << "Front value is " << v1.front() << endl;
    cout << "Last value is " << v1.back() << endl;
    vector<int>::iterator it = v1.begin();
    v1.insert(it + 3, 35);
    for (int i = 0; i < v1.size(); i++)
        cout << v1[i] << " ";
    cout << endl
         << endl;

    vector<string> v2(3, "Nikhil");
    cout << v2[0] << endl;
    cout << v2[1] << endl;
    cout << v2[2] << endl;
    cout << endl;

    vector<int> v3;
    cout << "Current capacity is " << v3.capacity() << endl;
    v3.push_back(10);
    cout << "Current capacity is " << v3.capacity() << endl;
    v3.push_back(20);
    cout << "Current capacity is " << v3.capacity() << endl;
    v3.push_back(30);
    cout << "Current capacity is " << v3.capacity() << endl;
    cout << endl;

    vector<int> v4;
    cout << "Current capacity is " << v4.capacity() << endl;
    for (int i = 0; i <= 9; i++)
        v4.push_back(10 * (i + 1));
    cout << "Current capacity is " << v4.capacity() << endl;
    v4.pop_back();
    cout << "After pop:" << endl;
    cout << "Current capacity is " << v4.capacity() << endl;
    v4.pop_back();
    cout << "Current capacity is " << v4.capacity() << endl;
    v4.pop_back();
    cout << "Current capacity is " << v4.capacity() << endl;
    v4.pop_back();
    cout << "Current capacity is " << v4.capacity() << endl;
    cout << "Total no. of elements are " << v4.size() << endl;
    cout << endl;

    vector<int> v5;
    for (int i = 0; i <= 9; i++)
        v5.push_back(10 * (i + 1));
    for (int i = 0; i < v5.size(); i++)
        cout << v5[i] << " ";
    cout << endl;
    v5.clear();
    cout << "After clear:" << endl;
    cout << "Current capacity is " << v5.capacity() << endl;
    cout << "Total no. of elements are " << v5.size() << endl;
}
