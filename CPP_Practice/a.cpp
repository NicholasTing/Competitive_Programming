#include <bits/stdc++.h>

using namespace std;

void solve() {
    int n,p,c;
    int prev_day_p=0;
    int prev_day_c=0;
    int possible = 1;
    cin >> n;
    while(n--){
        cin >> p >> c;
        if(p < prev_day_p){
            possible =0;
        }
        else if(c < prev_day_c){
            possible =0;
        }
        else if(c - prev_day_c > p - prev_day_p){
            possible = 0;
        }
        prev_day_p = p;
        prev_day_c = c;
    }
    if (possible){
        cout << "YES\n";
    } else{
        cout << "NO\n";
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

