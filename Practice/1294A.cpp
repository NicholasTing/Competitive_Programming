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
        
        ll a, b, c, n;

        cin >> a >> b >> c >> n;
        ll total = a + b + c + n;

        if (total % 3 == 0){
            
            ll target = total / 3;

            if (a > target || b > target || c > target) {
                cout << "NO\n";
            } else {
                ll aNeeded = target - a;
                ll bNeeded = target - b;
                ll cNeeded = target - c;

                if (aNeeded + bNeeded + cNeeded == n){
                    cout << "YES\n";
                }
                else {
                    cout << "NO\n";
                }

            }
        }
        else{
            cout << "NO\n";
        }
    }

    return 0;
}

