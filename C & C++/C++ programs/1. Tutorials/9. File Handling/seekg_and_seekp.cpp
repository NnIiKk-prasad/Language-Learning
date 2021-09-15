#include <fstream>
#include <iostream>
using namespace std;

int main()
{
    ifstream fin;
    fin.open("My_File.txt");
    
    fin.seekg(6);
    cout << fin.tellg() << " " << (char)fin.get() << endl;
    
    fin.seekg(2, ios_base::cur);
    cout << fin.tellg() << " " << (char)fin.get() << endl;

    fin.seekg(2, ios_base::beg);
    cout << fin.tellg() << " " << (char)fin.get() << endl;

    fin.seekg(-2, ios_base::end);
    cout << fin.tellg() << " " << (char)fin.get() << endl;

    fin.close();

    ofstream fout;
    fout.open("My_File.txt", ios::ate | ios::app);

    fout.seekp(2, ios_base::beg);
    cout << fout.tellp();
    return 0;
}
