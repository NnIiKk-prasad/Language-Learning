#include <iostream>
using namespace std;

class box
{
private:
    int l, b, h;

public:
    setDimention(int l, int b, int h)
    {
        this->l = l;
        this->b = b;
        this->h = h;
    }
    showDimention()
    {
        cout << "l = " << l << ", b = " << b << ", h = " << h;
    }
};

int main()
{
    box b1;
    b1.setDimention(56, 87, 34);
    b1.showDimention();
    return 0;
}
