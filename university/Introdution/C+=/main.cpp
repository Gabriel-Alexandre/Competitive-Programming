#include <iostream>

using namespace std;

int main() {
    unsigned long long  a, b, limit, maior, menor;
    unsigned int count = 0, n;

    cin >> n;

    while(n--) {
        cin >> a;
        cin >> b;
        cin >> limit;

        maior = a > b ? a : b;
        menor = a < b ? a : b;

        while(maior <= limit && menor <= limit) {
            menor += maior;
            count++;
            if(menor > limit)
                break;
            maior += menor;
            count++;
        }

        cout << count << endl;

        count = 0;
    }

    return 0;
}