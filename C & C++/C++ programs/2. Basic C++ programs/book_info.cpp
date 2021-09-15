#include <iostream>
using namespace std;

struct book
{
private:
    int bookid;
    char title[20];
    float price;

public:
    void input()
    {
        cout << "Enter bookid, title and price:\n";
        cin >> bookid >> title >> price;
        if (bookid < 0)
            bookid = -bookid;
    }
    void display()
    {
        cout << "\nBookid = " << bookid << ", "
             << "Title = " << title << ", "
             << "Price = " << price;
    }
};

main()
{
    book b1;
    b1.input();
    b1.display();
}
