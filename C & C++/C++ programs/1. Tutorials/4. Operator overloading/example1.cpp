#include <iostream>
using namespace std;

class Complex
{
    int a, b;

public:
    setdata(int x, int y)
    {
        a = x;
        b = y;
    }

    Complex operator+(Complex c)
    {
        Complex temp;
        temp.a = a + c.a;
        temp.b = b + c.b;
        return (temp);
    }

    void display()
    {
        cout << "a = " << a << ", b = " << b;
    }
};

int main()
{
    Complex c1, c2, c3;
    c1.setdata(3, 6);
    c2.setdata(7, 4);
    c3 = c1 + c2;
    c3.display();
    return 0;
}
