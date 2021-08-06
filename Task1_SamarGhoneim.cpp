#include <iostream>

using namespace std;

int hamming(string username, string twitter)
{
    int cnt=0;
    int userLen = username.length();
    int twiLen = twitter.length();
    for(int i=0;i<userLen; i++)
    {
        if(userLen==twiLen)
        {
            if(username[i]!=twitter[i])
            {
                cnt++;
            }
            else
            {
                continue;
            }
        }
        else
        {
            cnt=-1;
        }
    }
    return cnt;
}

void info(string name, string email, string username, string biostack, string twit)
{
    cout<< name<< ","<< email << ","<< username << ","<< biostack << ","<< twit << ","<< hamming(username,twit);
}

int main()
{
    string name = "Samar Ghoneim";
    string email= "samarghonaim27@gmail.com";
    string user = "@Samar";
    string bio = "Drug Development";
    string twit = "@SamG2";
    info(name,email,user,bio, twit);
    return 0;
}
