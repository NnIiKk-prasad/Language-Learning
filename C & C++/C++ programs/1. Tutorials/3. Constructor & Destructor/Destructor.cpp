#include <iostream>
using namespace std;

class Complex
{
    int a, b;

public:
    ~Complex()
    {
        cout << "Destructor called";
    }
};

void fun()
{
    Complex c;
}

int main()
{
    fun();
    return 0;
}
