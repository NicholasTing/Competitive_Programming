#include <bits/stdc++.h>
#include <iostream>

#define ll long long 

using namespace std;

int main() {

    std::ios_base::sync_with_stdio(false);
    int t;

    cin >> t;
    
    while(t--){

        ll n = 0;
        cin >> n;

        if (n % 2 == 0) {
            ll ans = n / 2;
            cout << ans << "\n";
        } else {
            ll ans = n / 2;
            cout << ans + 1 << "\n";
        }
 
    }

    return 0;
}


