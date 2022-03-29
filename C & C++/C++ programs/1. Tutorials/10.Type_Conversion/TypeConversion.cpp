#include <iostream>
using namespace std;

class Complex
{
    int a, b;

public:
    void setData(int x, int y)
    {
        a = x;
        b = y;
    }
    void showData()
    {
        cout << "a = " << a << ", b = " << b << endl;
    }
    operator int()
    {
        return a;
    }
    Complex() {}
    Complex(int x)
    {
        a = x;
        b = 0;
    }
};

int main()
{
    Complex c1, c2;

    c1.setData(3, 4);
    c1.showData();

    int x = 4;
    c1 = x; // constructor is called
    c1.showData();

    c2.setData(5, 6);
    c2.showData();
    
    int y;
    y = c2; // casting operator is called
    cout << "y = " << y << endl;
    return 0;
}
