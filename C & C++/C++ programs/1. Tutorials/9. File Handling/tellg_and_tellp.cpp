#include <fstream>
#include <iostream>
using namespace std;

int main()
{
    ifstream fin;
    fin.open("My_File.txt");
    int gpos;
    gpos = fin.tellg();
    cout << gpos << endl;
    fin.close();

    ofstream fout;
    fout.open("My_File.txt", ios::app);
    int ppos;
    ppos = fout.tellp();
    cout << ppos << endl;
    fout << " Prasad";
    ppos = fout.tellp();
    cout << ppos;
    fin.close();

    return 0;
}
