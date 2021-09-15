#include <fstream>
#include <iostream>
using namespace std;

int main()
{
    ofstream fout;
    fout.open("My_File.dat");
    fout << "Hello";
    fout.close();
    return 0;
}
