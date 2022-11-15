#include <bits/stdc++.h>
#include <iostream>

#define getunique(v) {sort(all(v)); v.erase(unique(all(v)), v.end());}

typedef long long ll;
typedef long double lld;

using namespace std;

const lld pi = 3.14159265358979323846;
const ll mod = 1000000007;
// const ll mod = 998244353;
// ll mod;

ll n, m, k, q, l, r, x, y, z;

// Problem - https://codeforces.com/gym/344975/problem/B

void solve(int tc = 0) {

    cin >> n >> k;

    ll ans = 1;

    for (ll i =0; i < k; i++){
        ans = (ans * n) % mod;
    }

    cout << ans << "\n";

}

int main(){

    std::ios_base::sync_with_stdio(false);

    int tc;

    cin >> tc;

    for(int t = 0; t < tc; t++){
        solve(t);
    }

    return 0;

}
