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
    showData()
    {
        cout << "\na = " << a << ", b = " << b;
    }
    friend Complex operator+(Complex, Complex);
    friend Complex operator-(Complex);
};

Complex operator+(Complex X, Complex Y)
{
    Complex temp;
    temp.a = X.a + Y.a;
    temp.b = X.b + Y.b;
    return (temp);
}

Complex operator-(Complex X)
{
    Complex temp;
    temp.a = -X.a;
    temp.b = -X.b;
    return (temp);
}

int main()
{
    Complex c1, c2, c3;
    c1.setData(3, 6);
    c2.setData(7, 4);
    c3 = c1 + c2; // c3 = operator+(c1,c2);
    c3.showData();
    c3 = -c3; // c3 = operator-(c3);
    c3.showData();
    return 0;
}
