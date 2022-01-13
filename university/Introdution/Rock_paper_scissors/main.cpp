#include <iostream>

using namespace std;

int main() {
    string fyodor, matroskin, sharic;
    string jogo[3];
    int r = 0, p = 0, s = 0;

    // 0 = fyodor
    // 1 = matroskin
    // 2 = sharic

    getline(cin, fyodor);
    jogo[0] = fyodor;
    getline(cin, matroskin);
    jogo[1] = matroskin;
    getline(cin, sharic);
    jogo[2] = sharic;

    for(int i = 0; i < 3; i++) {
        if(jogo[i] == "rock")
            r++;
        if(jogo[i] == "paper")
            p++;
        if(jogo[i] == "scissors")
            s++;
    }

    if ((r == 3 || p == 3 || s == 3) || 
        (r == 1 && p == 1 && s == 1) ||
        (p == 2 && r == 1) ||
        (s == 2 && p == 1) ||
        (r == 2 && s == 1)) {
        cout << "?\n";
    }else if (p == 2 && fyodor == "scissors") {
        cout << "F\n";
    }else if (p == 2 && matroskin == "scissors") {
        cout << "M\n";
    }else if (p == 2 && sharic == "scissors") {
        cout << "S\n";
    }else if (r == 2 && fyodor == "paper") {
        cout << "F\n";
    }else if (r == 2 && matroskin == "paper") {
        cout << "M\n";
    }else if (r == 2 && sharic == "paper") {
        cout << "S\n";
    }else if (s == 2 && fyodor == "rock") {
        cout << "F\n";
    }else if (s == 2 && matroskin == "rock") {
        cout << "M\n";
    }else if (s == 2 && sharic == "rock") {
        cout << "S\n";
    }

    return 0;
}