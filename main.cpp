#include <iostream>

using namespace std;

void info(string name, string email, string username, string biostack)
{
    cout<< name<< " "<< email << " "<< username<< " "<<biostack;
}

int main()
{
    string name = "Samar Ghoneim,";
    string email= "samarghonaim27@gmail.com,";
    string user = "@Samar,";
    string bio = "Drug Development";
    info(name,email,user,bio);
    return 0;
}
