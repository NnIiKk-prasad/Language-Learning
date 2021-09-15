#include <iostream>
using namespace std;

int area(int, int);
float area(int);

float area(int r)
{
    return (3.14 * r * r);
}

int area(int l, int b)
{
    return (l * b);
}

int main()
{
    int r;
    cout << "Enter radius of a circle: ";
    cin >> r;
    float A = area(r);
    cout << "Area of the circle is " << A << endl;
    int l, b, a;
    cout << "\nEnter length and breadth of a rectangle:\n";
    cin >> l >> b;
    a = area(l, b);
    cout << "Area of rectangle is " << a << endl;
    return 0;
}
