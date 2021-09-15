#include <iostream>
using namespace std;

class Empty
{
};

main()
{
    Empty a, b;
    cout << &a << " " << &b;
    cout << "\n"
         << sizeof(Empty);
}
