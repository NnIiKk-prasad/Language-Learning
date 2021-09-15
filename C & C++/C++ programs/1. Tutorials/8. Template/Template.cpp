#include <iostream>
using namespace std;

template <class X>
X big(X a, X b)
{
    if (a > b)
        return a;
    else
        return b;
}

int main()
{
    cout << big(6, 9) << endl;
    cout << big(5.43, 7.5) << endl;
    return 0;
}
