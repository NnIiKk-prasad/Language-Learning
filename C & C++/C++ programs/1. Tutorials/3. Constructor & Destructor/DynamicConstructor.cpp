#include <iostream>
using namespace std;

class A
{
    int a, b;
    int *p;

public:
    A() // dynamic constructor
    {
        a = 0;
        b = 0;
        p = new int;
    }
    A(int x, int y, int z) // dynamic constructor
    {
        a = x;
        b = y;
        p = new int;
        *p = z;
    }
    ~A()
    {
        delete p;
    }
};

int main()
{
    A o1, o2(3, 4, 5);
    return 0;
}
