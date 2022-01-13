#include <iostream>
#include <string>

using namespace std;

int main() {
    string name;

    getline(cin, name);

    if (name == "Hello,World!") {
        cout << "AC" << endl;
    }else {
        cout << "WA" << endl;
    }
}