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
    
    ll n = 0;
    ll q = 0;
    // Solve here
    while(t--){
        cin >> n >> q;

        ll total = n;
        ll a[n];
        ll j = 0;
        while (j < n){
            cin >> a[j++];
        }
        while (q--){

            ll final_ans = 0;
            ll addEven = 0;
            ll addOdd = 0;
            ll type = -1;
            ll num = 0;

            cin >> type >> num;
            if (type == 0){
                addEven += num;
            }
            else {
                addOdd += num;
            }

            for (ll i = 0; i < total; i++){
                if (a[i] % 2 == 0){
                    a[i] = a[i] + addEven;
                } else {
                    a[i] = a[i] + addOdd;
                }
            }

            for (ll i =0; i < total; i++){
                final_ans += a[i];
            }

            cout << final_ans << "\n";
        }

    }

    return 0;
}

