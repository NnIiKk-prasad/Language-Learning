#include <iostream>
using namespace std;

class Complex
{
private:
    int a, b;

public:
    friend istream &operator>>(istream &, Complex &);
    friend ostream &operator<<(ostream &, Complex);
};

istream &operator>>(istream &din, Complex &C)
{
    cin >> C.a >> C.b;
    return (din);
}

ostream &operator<<(ostream &dout, Complex C)
{
    cout << C.a << " + " << C.b << "j";
    return (dout);
}

int main()
{
    Complex c1;
    cout << "Enter values of 'a' & 'b' of complex number (a + bj):\n";
    cin >> c1; // operator>>(cin, c1);
    cout << "\nThe complex number is: ";
    cout << c1; // operator<<(cout, c1);
    return 0;
}
