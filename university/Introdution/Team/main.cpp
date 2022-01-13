#include <iostream>

using namespace std;

int main() {
    int alunos[3], in, count = 0, point = 0;

    cin >> in;

    while(in--) {
        cin >> alunos[0] >> alunos[1] >> alunos[2];

        for(int i = 0; i < 3; i++) {
            if (alunos[i] == 1) 
                count++;
        }

        if (count >= 2)
            point++;
        
        count = 0;
    }

    cout << point << '\n';

    return 0;
}