#include <iostream>
using namespace std;

class A
{
    int *p;

public:
    A()
    {
        cout << "Constructor A" << endl;
        p = new int;
    }
    virtual ~A()
    {
        cout << "Destructor A" << endl;
        delete p;
    }
};

class B : public A
{
    int *q;

public:
    B()
    {
        cout << "Constructor B" << endl;
        q = new int;
    }
    ~B()
    {
        cout << "Destructor B" << endl;
        delete q;
    }
};

void fun1()
{
    A *ptr;
    ptr = new B;
    delete ptr;
}

int main()
{
    fun1();
}
