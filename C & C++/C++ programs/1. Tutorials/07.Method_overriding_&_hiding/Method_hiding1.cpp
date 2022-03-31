#include <iostream>
using namespace std;

class Base
{
public:
    int fun()
    {
        cout << "Base::fun() called";
    }
    int fun(int i)
    {
        cout << "Base::fun(int i) called";
    }
};

class Derived : public Base
{
public:
    int fun() // it hides both fun() and fun(int) of base class.
    {
        cout << "Derived::fun() called";
    }
};

int main()
{
    Derived d;
    // d.fun(5); // error
    d.Base::fun(5);
    return 0;
}