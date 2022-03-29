#include <iostream>
using namespace std;

class Complex
{
    int a, b;

public:
    setData(int x, int y)
    {
        a = x;
        b = y;
    }
    void showData()
    {
        cout << " a = " << a;
    }
    friend void fun(Complex);
};

void fun(Complex c)
{
    cout << "Sum is " << c.a + c.b;
}

int main()
{
    Complex c1;
    c1.setData(3, 4);
    fun(c1);
    return 0;
}
