#include <iostream>

int main() {
    unsigned long long n, m, a, i, j, con = 1, com = 1;

    std::cin >> n;
    std::cin >> m;
    std::cin >> a;

    for(i = a; i < n; i += a) {
        con++;
    }

    for(j = a; j < m; j += a) {
        com++;
    }
    
    std::cout << con * com << std::endl;

    return 0;
}