#include <iostream>
using namespace std;

class A
{
private:
    int a;

protected:
    void setValue(int x)
    {
        a = x;
    }
    int getValue()
    {
        return a;
    }
};

class B : public A
{
public:
    void setData(int k)
    {
        setValue(k);
    }
    int getData()
    {
        return getValue();
    }
};

int main()
{
    B obj;
    obj.setData(6);
    cout << obj.getData();
    return 0;
}
