#include <iostream>
using namespace std;

class A
{
public:
    virtual void f1() { cout << "A f1" << endl; }
    void f2() { cout << "A f2" << endl; }
};

class B : public A
{
public:
    void f1() { cout << "B f1" << endl; }          // method overriding
    void f2(int x = 0) { cout << "B f2" << endl; } // method hiding
};

int main()
{
    A *p, obj1;
    B obj2;
    p = &obj2;
    obj2.f1(); // early binding
    obj2.f2(); // early binding
    p->f1();   // late binding

    return 0;
}
