#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>
using namespace std;
int len_result = 0;
int count_result = 0;
string substr;
string substr_2;
int andis_tedad;
int andis_zirmatn;
int len(string matn);
int count(string matn , string zir_matn);

int main()
{
    std::cout << "please enter your text!\n";
    string txt;
    getline(cin , txt);
    cout << "what are you looking for?\n";
    string zir_reshteh;
    getline(cin , zir_reshteh);
    cout << "there are " << count(txt,zir_reshteh) <<  " "  << zir_reshteh << " in your text!!!\n";
    return 0;
}
int len(string matn)
{
    len_result = 0;
    matn += "^";
for (int i = 0; i < 1000; i++)
    {
        substr = matn[i];
        if (substr == "^")
            break;
        else
            len_result +=1;
    }

    return len_result;

}
int count(string matn , string zir_matn)
{   
    count_result = 0;
    int x = len(matn) + 1;
    int andazeh = len(zir_matn);
    for (int i = 0; i < x ; i++)
    {
        if (andis_tedad == andazeh)
        {
            count_result += 1;
            andis_tedad = 0;
            andis_zirmatn = 0;   
        }
        substr = matn[i];
        substr_2 = zir_matn[andis_zirmatn];
        if (substr == substr_2)
        {
            andis_tedad += 1;
            andis_zirmatn += 1;
        }
        else
        {
            andis_tedad = 0;
            andis_zirmatn = 0;
        }
    }
    return count_result;
}