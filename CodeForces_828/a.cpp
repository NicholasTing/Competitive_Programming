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
        ll a[50];
        ll i = 0;

        map<int, set<char>> test;
        test.clear();

        while (n--) {
            cin >> a[i];
            i++;
        }
        string words;
        cin >> words;

        bool found = false;
        for (ll i = 0; i < words.length(); i++) {
            char word = words[i];
            ll num = a[i];
            for (ll j = 0; j < words.length(); j++){
                if (words[i] == words[j] && num[i] != num[j]){
                    found = true;
                    break
                }
            }
        }

        if (not found){
            cout << "YES\n";
        }


    }

    return 0;
}

