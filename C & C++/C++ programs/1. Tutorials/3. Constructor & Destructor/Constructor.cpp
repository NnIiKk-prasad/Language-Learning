#include <iostream>
using namespace std;

class Complex
{
    int a, b;

public:
    Complex(int x, int y) //Parameterized constructor
    {
        a = x;
        b = y;
    }
    Complex(int x) //Parameterized constructor
    {
        a = x;
    }
    Complex() //Default constructor
    {
    }
    Complex(Complex &c) //Copy constructor
    {
        a = c.a;
        b = c.b;
    }
};

int main()
{
    Complex c1(3, 5), c2(6), c3;
    Complex c4 = c1;
    return 0;
}
