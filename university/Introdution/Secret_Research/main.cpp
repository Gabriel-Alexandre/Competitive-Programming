#include <iostream>
#include <string>

using namespace std;

int main() {
    string in;
    string auxDP, auxP, auxU, auxNc;
    int n;

    cin >> n;
    getchar();

    while(n--) {

        getline(cin, in);

        auxP = in[0]; // (Primeria posição)
        auxU = in[in.size()-1]; // (Última posição)

        if(in.size() > 2) {
            auxDP = in.substr(in.size()-2, in.size()); // (Duas últimas posições)
            if(in.size() >= 3)
                auxNc = in.substr(0, 3); // (Três primeiras posições)   
        }

        if (in == "1" || in == "4" || in == "78") {
            cout << "+\n";
        }else if(auxDP == "35") {
            cout << "-\n";
        }else if((auxP == "9" && auxU == "4")) {
            cout << "*\n";
        }else if(auxNc == "190") {
            cout << "?\n";
        }else {
            cout << "+\n";
        }
    }

    return 0;
}