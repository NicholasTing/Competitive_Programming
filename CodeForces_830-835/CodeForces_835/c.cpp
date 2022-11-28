#include <vector>
#include <iostream>
#include <algorithm>

#define ll long long 

using namespace std;

int main() {

    std::ios_base::sync_with_stdio(false);
    int t;

    cin >> t;
    
    while(t--){

        ll n;
        cin >> n;
        vector<ll> a;
        vector<ll> p;
        a.clear();
        p.clear();
        ll n1;

        ll highest = 0;
        ll secondHighest = 0;
        for (ll i = 0; i < n; i++){
            cin >> n1;
            a.push_back(n1);
            p.push_back(n1);
        } 

        sort(a.begin(), a.end());

        ll h = a[n-1];
        ll sh = a[n-2];

        for (ll i = 0; i < n; i++){
            if(p[i] == h){
                cout << p[i] - sh << " ";
            }
            else{
                cout << p[i] - h << " ";
            }
        } 

        cout << "\n";
    }

    return 0;
}


