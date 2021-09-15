// Quizzes - Guess the output

/*#include <iostream>
using namespace std;
typedef void (*FunPtr)(int);
int Look(int = 10, int = 22);
void Note(int);
int main()
{
    FunPtr ptr = Note;
    (*ptr)(40);
    return 0;
}
int Look(int x, int y)
{
    return (x + y % 20);
}
void Note(int x)
{
    cout << Look(x) << endl;
}*/

/*#include<iostream>
using namespace std;
class BaseCounter
{
    protected:
        long int count;
    public:
        void CountIt(int x, int y = 10, int z = 20)
        { count = 0; cout<< x << " " << y << " " << z << endl; }
        BaseCounter()
        { count = 0; }
        BaseCounter(int x)
        { count = x ; }
};
class DerivedCounter: public BaseCounter
{
    public:
        DerivedCounter() { }
        DerivedCounter(int x): BaseCounter(x) { }
};
int main()
{
    DerivedCounter objDC(30);
    objDC.CountIt(40, 50);
    return 0;
}*/

/*#include<iostream>
using namespace std;

class base {
int arr[10];
};

class b1: virtual public base { };

class b2: virtual public base { };

class derived: public b1, public b2 {};

int main(void)
{
cout<<sizeof(derived);
return 0;
}*/

/*#include<iostream>
using namespace std;
class base
{
public:
    int *ptr;
    int x;
    base()
    {
        x=5;
        ptr = &x;
    }
    base(const base &p){ this->x = p.x; }
};
int main()
{
    base b1;
    cout<<*b1.ptr<<endl;
    base b2 = b1;
    cout<<*b2.ptr<<endl;
    *b1.ptr=10;
    cout<<*b2.ptr;
    return 0;
}*/

/*#include<iostream>
using namespace std;
class Test
{
public:
    Test() { cout<<"constructor called"; }
private:
    ~Test() {}
friend void destructTest(Test* );
};
 // Only this function can destruct objects of Test
void destructTest(Test* ptr)
{
    delete ptr;
}
 int main()
{
    Test *ptr = new Test;
    destructTest (ptr);
    Test *p = (Test*)malloc(sizeof(Test));
    destructTest(p);
    //Test obj; //error
    return 0;
}*/

/*#include<iostream>
using namespace std;
int main()
{
    int array1[] = {1, 5, 6, 8};
    int array2[] = {2, 3, 9, 1, 10};
    int arr[9];
    for(int i = 0; i < 4; i++)
    {
        arr[i] = array1[i];
    }
    for(int i = 0; i < 5; i++)
    {
        arr[i + 4] = array2[i];
    }
    for(int round = 1; round < 8; round++)
    {
        for(int i = 0; i < 8 - round; i++)
        {
            if(arr[i] > arr[i + 1])
            {
                int t = arr[i];
                arr[i] = arr[i + 1];
                arr[i + 1] = t;
            }
        }
    }
    for(int i = 0; i < 9; i++)
    {
        cout<<arr[i]<<" ";
    }
    return 0;
}*/

/*#include<iostream>
using namespace std;
class A
{
    int *x;
    A *y;
};
int main()
{
    cout<<sizeof(A);
}*/
