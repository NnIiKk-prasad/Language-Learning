#include <iostream>
#include <map>
using namespace std;

int main()
{
    /*map<int, string> Customer;
    Customer[100] = "Gajendra";
    Customer[123] = "Dilip";
    Customer[148] = "Adita";
    Customer[171] = "Shahid";
    Customer[200] = "Rajesh";*/
    map<int, string> Customer = {{100, "Gajendra"}, {123, "Dilip"}, {148, "Adita"}, {171, "Shahid"}, {200, "Rajesh"}};
    Customer.insert(pair<int, string>(208, "Saurabh"));
    map<int, string>::iterator p = Customer.begin();
    while (p != Customer.end())
    {
        cout << p->first << " " << p->second << endl;
        p++;
    }
    cout << Customer.at(148) << endl;
    cout << Customer.size() << endl;
    cout << Customer.empty() << endl;
}
