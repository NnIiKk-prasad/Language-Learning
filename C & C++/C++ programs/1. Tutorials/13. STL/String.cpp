#include <iostream>
#include <string>
using namespace std;

int main()
{
    string s1;
    s1 = "Hello "; // or s1.assign("Hello");

    string s2;
    cout << "Enter your name: ";
    cin >> s2;

    string s3 = s1 + s2; // or s1.append(s2);
    cout << s3 << endl;
    s3.erase();

    s1.insert(5, "!");
    cout << s1 << endl;

    s1.replace(2, 2, "A");
    cout << s1 << endl;

    string s = "Hello online online students";
    cout << s.find("online") << endl
         << s.rfind("online") << endl;

    cout << s.size() << endl;

    string str1 = "Amit";
    string str2 = "Amar";
    cout << str2.compare(str1) << endl;
}
