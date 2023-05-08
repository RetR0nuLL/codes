#include <iostream>
int len_result;
std::string substr;
int len(std::string matn)
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