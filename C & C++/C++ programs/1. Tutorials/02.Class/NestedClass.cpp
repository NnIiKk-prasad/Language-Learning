#include <iostream>
#include <string.h>
using namespace std;

class Student
{
    int rollNo;
    char name[20];
    class Address
    {
        int HouseNo;
        char street[20];
        char city[20];
        char state[20];
        char pinCode[7];

    public:
        void setAddress(int h, const char *s, const char *c, const char *st, const char *p)
        {
            HouseNo = h;
            strcpy(street, s);
            strcpy(city, c);
            strcpy(state, st);
            strcpy(pinCode, p);
        }
        void showAddress()
        {
            cout << " Address:" << endl;
            cout << "  " << HouseNo << endl;
            cout << "  " << street << " " << city << endl;
            cout << "  " << state << " " << pinCode << endl;
        }
    };
    Address add;

public:
    void setRoll(int r)
    {
        rollNo = r;
    }
    void setName(const char *n)
    {
        strcpy(name, n);
    }
    void setAddress(int h, const char *s, const char *c, const char *st, const char *p)
    {
        add.setAddress(h, s, c, st, p);
    }
    void showStudent()
    {
        cout << "Student Data:" << endl;
        cout << " Name: " << name << endl;
        cout << " Roll no.: " << rollNo << endl;
        add.showAddress();
    }
};

int main()
{
    Student s1;
    s1.setRoll(50);
    s1.setName("Nikhil Prasad");
    s1.setAddress(51, "Jeevan Bhima Nagar", "Bangalore", "Karnataka", "560075");
    s1.showStudent();
}
