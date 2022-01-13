#include <iostream>
#include <stdio.h>

using namespace std;

int main() {
    int num, numCall, mile = 0, juice = 0, x, aux, auy;

    cin >> num;
    
    int mileArray[num], juiceArray[num];

    for(int i = 0; i < num; i++) {
        cin >> numCall;

        while(numCall--) {
            cin >> x;

            aux = (((x/30) * 10) + 10);
            auy = (((x/60) * 15) + 15);

            mile += aux;
            juice += auy;
        }
        
        mileArray[i] = mile;
        juiceArray[i] = juice;
        mile = 0;
        juice = 0;
    }

    for(int i = 0; i < num; i++) {
        if(mileArray[i] < juiceArray[i]) {
            printf("Case %d: Mile %d\n", i+1, mileArray[i]);
        }else if (mileArray[i] > juiceArray[i]) {
            printf("Case %d: Juice %d\n", i+1, juiceArray[i]);
        }else {
            printf("Case %d: Mile Juice %d\n", i+1, mileArray[i]);
        }
    }

    return 0;
}