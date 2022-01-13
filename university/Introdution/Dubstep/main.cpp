#include <iostream>
#include <string>

using namespace std;

int main() {
    string in, aux;

    aux = "WUB";

    getline(cin, in);

    while(1) {
        if (in.find("WUB") == std::string::npos)
            break;

        in.replace(in.find(aux), aux.length(), " ");

        if(in[0] == ' ') {
            aux = " ";
            in.replace(in.find(aux), aux.length(), "");
        }
        aux = "WUB";
    }

    cout << in << endl;

    return 0;
}