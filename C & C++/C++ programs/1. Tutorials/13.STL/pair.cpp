#include <iostream>
using namespace std;

class student
{
    string name;
    int age;

public:
    void setStudent(string n, int a)
    {
        name = n;
        age = a;
    }
    void showStudent()
    {
        cout << "Name: " << name << " & Age: " << age;
    }
};

int main()
{
    pair<string, int> p1;
    pair<string, string> p2;
    pair<int, student> p3;
    p1 = make_pair("Nikhil", 50);
    p2 = make_pair("India", "New Delhi");
    student s;
    s.setStudent("Nikhil", 21);
    p3 = make_pair(1, s);

    cout << "\nPair 1:\n";
    cout << "  " << p1.first << ", " << p1.second << endl;
    cout << "\nPair 2:\n";
    cout << "  " << p2.first << ", " << p2.second << endl;
    cout << "\nPair 3:\n";
    cout << "  " << p3.first << ", ";
    p3.second.showStudent();
    return 0;
}
