#include <iostream>
#include <conio.h>


/*
HAŁWA WIELKIEJ POLSCE
*/


using namespace std;


struct Brackets{

int Left;
int Right;

};

struct Operation
{
    string Number1; /// *sax solo* WE ARE NUMBER ONE NUMBER ONE
    string Number2;
    string Operator;
};


class MarszNiepodleglosci{

//private:
public:
string pdw;

string wolnaPolska;

public:
MarszNiepodleglosci(string pdw)
{
    this -> pdw = pdw;
    this -> wolnaPolska = "";
}

Brackets szukajKonfidenta()
{
    int i = 0;
    int lastOpenBracket = 0;
    do
    {
        if(pdw[i] == '(')
        {
            lastOpenBracket = i;
        }
        i++;
    }
    while(pdw[i] != ')');

    Brackets result;
    result.Left = lastOpenBracket;
    result.Right = i;

    return result;
}

Operation znajdzTeczki(Brackets nawiasy)
{
    Operation teczkaZSzafy;
    teczkaZSzafy.Number1 = pdw[nawiasy.Left+1];
    teczkaZSzafy.Operator = pdw[nawiasy.Left+2];
    teczkaZSzafy.Number2 = pdw[nawiasy.Right-1];

    return teczkaZSzafy;
}



};


int main()
{
    MarszNiepodleglosci prowokacja("(1+2*(3+6))");
    
    /// 3 6 + 2 * 1 +

    while(true)
    {

    Brackets nawiasy = prowokacja.szukajKonfidenta();


    Operation TWBolek = prowokacja.znajdzTeczki(nawiasy);
    prowokacja.wolnaPolska += TWBolek.Number1 + " " + TWBolek.Number2 + " " + TWBolek.Operator + " ";

    prowokacja.pdw.erase(nawiasy.Left,  nawiasy.Right - nawiasy.Left);

    cout << "NAWIASY " << nawiasy.Left << " " << nawiasy.Right << endl;
    cout << "WYNIK " << prowokacja.wolnaPolska << endl;
    cout << "POZOSTALO " << prowokacja.pdw << endl;
    getch();
    }

    return 0;
}
