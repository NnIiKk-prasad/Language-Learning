#include <iostream>
using namespace std;

class Complex
{
    int a;

public:
    setData(int x)
    {
        a = x;
    }

    Complex operator++() //pre increment
    {
        Complex temp;
        temp.a = ++a;
        return (temp);
    }

    Complex operator++(int) //post increment
    {
        Complex temp;
        temp.a = a++;
        return (temp);
    }

    void showData()
    {
        cout << " a = " << a << endl;
    }
};

int main()
{
    Complex c1, c2, c3;
    c1.setData(3);
    c2 = ++c1;
    c3 = c1++;
    c1.showData();
    c2.showData();
    c3.showData();
    return 0;
}
