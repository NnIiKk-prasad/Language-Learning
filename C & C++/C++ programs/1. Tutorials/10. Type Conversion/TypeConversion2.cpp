#include <iostream>
using namespace std;

class Item
{
    int a, b;

public:
    void showData()
    {
        cout << "a = " << a << ", b = " << b << endl;
    }
    void setA(int x)
    {
        a = x;
    }
    void setB(int y)
    {
        b = y;
    }
};

class Product
{
    int m, n;

public:
    void setData(int x, int y)
    {
        m = x;
        n = y;
    }
    operator Item()
    {
        Item t;
        t.setA(this->m);
        t.setB(this->n);
        return t;
    }
};

int main()
{
    Item i1;
    Product p1;
    p1.setData(3, 4);
    i1 = p1; // casting operator is called
    i1.showData();
    return 0;
}
