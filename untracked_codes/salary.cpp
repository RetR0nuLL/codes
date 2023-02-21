#include <iostream>
#include <string>
using namespace std;
int convert(int f_temp)
{
    int hour;
    int min;
hour = (int(f_temp / 100));
min = f_temp%100;
return ((hour *60)+min);

}
int main()
{   
    cout << "what is the name?\n:";
    std::string name;
    cin >> name;
    cout << "how maany days did " << name <<" work?\n:";
    int days;
    cin >> days;
    int meqdar_araye = days *2;
    int araye[meqdar_araye];
    int temp = 0;
    for (int i = 1; i <= meqdar_araye; i++)
    {
        if ((i % 2) != 0)
        {
        cout << "\ntime of entrance:";
        cin >> temp;
        araye[i - 1] = convert(temp);
        temp = 0;
        }
        if ((i % 2) == 0)
        {
        cout << "\ntime of exiting:";
        cin >> temp;
        araye[i - 1] = convert(temp);
        temp = 0;
        }
    }
    int minsum =0;
    for (int i = 0; i < meqdar_araye; i+=2)
    {
        minsum += araye[i+1] - araye[i];
    }
    int saatkar = int(minsum /60);
    int daqiqekar = minsum%60;
    double salary = (saatkar *20000);
    salary += ((daqiqekar/60) * 20000);
    cout << "your salary is " << salary <<" toman";
    
    
    return 0;
}