#include <iostream>
#include <string>

using namespace std;

int main() {
    string name;
    string p = "aeiou13579"; // Se for uma vogal ou um número impar a carta precisa ser virada
    int count = 0;

    getline(cin, name);

    for(int i = 0; i < name.size(); i++) {
        for(int j = 0; j < p.size(); j++) {
            if(name[i] == p[j]) {
                count++;
            }
        }
    }

    cout << count << endl;

    return 0;
}