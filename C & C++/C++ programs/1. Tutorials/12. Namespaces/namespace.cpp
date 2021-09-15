#include <iostream>
using namespace std;

namespace MySpace
{
    int a;
    int f1();
    class A
    {
    public:
        void f2();
    };
}

int MySpace::f1()
{
    cout << "f1() in MySpace" << endl;
}

void MySpace::A::f2()
{
    cout << "f2() of class A in MySpace" << endl;
}

using namespace MySpace;

int main()
{
    a = 5;
    f1();
    A obj;
    obj.f2();
    return 0;
}
