#include <iostream>

using namespace std;

int main() {
    string in, first, end;
    int aux, n;

    cin >> n;
    getchar();

    while(n--) {
        getline(cin, in);

        if(in.size() > 10) {
            first = in[0];
            end = in[in.size()-1];
            aux = in.size() - 2;

            cout << first << aux << end << endl;
        }else {
            cout << in << endl;
        }
    }

    return 0;
}