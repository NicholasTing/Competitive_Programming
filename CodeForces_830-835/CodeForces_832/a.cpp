#include <bits/stdc++.h>
#include <iostream>

#define ll long long

using namespace std;

// Problem - https://codeforces.com/contest/1747/problem/A

int main() {

    std::ios_base::sync_with_stdio(false);
    cout << setprecision(15) << fixed;
    cin.tie(NULL);

    ll t;

    cin >> t;
    
    // Solve here
    while(t--){

        ll n;
        cin >> n;
        ll total = 0;
        ll a;
        while (n--) {
            cin >> a;
            total = total + a;
        }

        cout << abs(total) << "\n";

    }

    return 0;
}

