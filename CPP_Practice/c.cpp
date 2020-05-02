// Powered Addition
// https://codeforces.com/contest/1339/problem/C

#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

void solve() {
    int n;
    cin >> n;
    vector<ll> ans;
    ll i;
    int ordered = 1;
    while(n--){
        cin >> i;
        ans.push_back(i);
    }
    int prev = -1;
    // if it is ordered in the first place, we can just return true

    int max_diff = 0;
    ll first = ans[0];
    int count = 0;
    while(n < 30 && ordered == 0){
        for(int i =0; i< n-1;i++){
            
        }
    }

    }
    
    if(ordered){
        cout << 0 << "\n";
    }
}

int main()
{

#ifndef ONLINE_JUDGE
    freopen ("input.txt","r",stdin);
    freopen ("output.txt","w",stdout);
#endif
    int t;
    cin >> t;
    while(t--){
        solve();
    }  
}