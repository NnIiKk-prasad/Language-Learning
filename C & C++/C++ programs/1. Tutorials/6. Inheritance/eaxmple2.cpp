#include <iostream>
using namespace std;

class A
{
    int a;

public:
    void display()
    {
        cout << "a = " << a;
    }
    A(int k)
    {
        a = k;
    }
    ~A()
    {
    }
};

class B : public A
{
    int b;

public:
    void showValue()
    {
        display();
        cout << ", b = " << b;
    }
    B(int x, int y) : A(x)
    {
        b = y;
    }
    ~B()
    {
    }
};

int main()
{
    B obj(2, 6);
    obj.showValue();
    return 0;
}
