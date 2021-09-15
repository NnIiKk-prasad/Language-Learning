#include <iostream>
#include <list>
using namespace std;

int main()
{
    list<string> l1{"New Delhi", "Dhaka", "Islamabad", "Kathmandu"};
    l1.push_back("Karanchi");
    l1.push_front("New York");
    list<string>::iterator p = l1.begin();
    while (p != l1.end())
    {
        cout << *p << " ";
        p++;
    }
    cout << "\nTotal no. of elements are " << l1.size() << endl;
    
    l1.pop_front();
    l1.pop_back();
    list<string>::iterator q = l1.begin();
    while (q != l1.end())
    {
        cout << *q << " ";
        q++;
    }
    cout << "\nTotal no. of elements are " << l1.size() << endl
         << endl;

    list<int> l2{55, 22, 77, 44, 66, 99, 44, 11};
    list<int>::iterator r = l2.begin();
    while (r != l2.end())
    {
        cout << *r << " ";
        r++;
    }
    cout << endl;
    l2.sort();
    list<int>::iterator s = l2.begin();
    while (s != l2.end())
    {
        cout << *s << " ";
        s++;
    }
    cout << endl;
    l2.reverse();
    list<int>::iterator t = l2.begin();
    while (t != l2.end())
    {
        cout << *t << " ";
        t++;
    }
    cout << endl;
    l2.remove(44);
    list<int>::iterator u = l2.begin();
    while (u != l2.end())
    {
        cout << *u << " ";
        u++;
    }
    cout << endl;
    l2.clear();
    list<int>::iterator v = l2.begin();
    while (v != l2.end())
    {
        cout << *v << " ";
        v++;
    }
    cout << endl;
}
