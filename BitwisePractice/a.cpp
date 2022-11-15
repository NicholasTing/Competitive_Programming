#include <bits/stdc++.h>
#include <iostream>

#define ll long long

using namespace std;

// Problem - https://codeforces.com/gym/344975/problem/A
// 800 Rated

int main() {

    std::ios_base::sync_with_stdio(false);
    int t;
    ll n;

    cin >> t;
    
    while(t--){
        
        cin >> n;

        ll a[n];
        ll ans;

        for (int i = 0; i < n; i++){
            cin >> a[i];
        }
        
        ans = a[0];
        
        for (int i = 0; i < n; i++){
            ans &= a[i];
        }

        cout << ans << "\n";
    }

    return 0;
}

