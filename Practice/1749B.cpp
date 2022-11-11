#include <bits/stdc++.h>
#include <iostream>

#define ll long long 

using namespace std;

// Problem - https://codeforces.com/problemset/problem/1749/B
// 900 Rated

// Personal learnings from this round
// Initially I started off with saving variables in an array like this
// int a[n] ... cin >> a[i];
// But that took a little bit too long and caused time limit exceeded

int main() {

    std::ios_base::sync_with_stdio(false);
    int t;

    cin >> t;
    
    while(t--){

        // Remember to use long long to prevent integer overflow
        ll n;
        ll a, b;

        cin >> n;

        // Declaring variables as 0 is important otherwise its a different number
        ll total = 0;
        ll highest = 0;
        
        for (ll i = 0; i < n; i++) {
            cin >> a;
            total += a;
        }

        for (ll i = 0; i < n; i++) {
            cin >> b;
            total += b;
            highest = max(highest, b);
        }   

        ll answer = total - highest;

        cout << answer << "\n";
    }

    return 0;
}


