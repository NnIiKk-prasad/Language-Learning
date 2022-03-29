#include <iostream>
using namespace std;

class Product
{
    int m, n;

public:
    void setData(int x, int y)
    {
        m = x;
        n = y;
    }
    int getM()
    {
        return m;
    }
    int getN()
    {
        return n;
    }
};

class Item
{
    int a, b;

public:
    void showData()
    {
        cout << "a = " << a << ", b = " << b << endl;
    }
    Item() {}
    Item(Product p)
    {
        a = p.getM();
        b = p.getN();
    }
};

int main()
{
    Item i1;
    Product p1;
    p1.setData(3, 4);
    i1 = p1; // constructor is called
    i1.showData();
    return 0;
}
