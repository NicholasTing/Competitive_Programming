#include <vector>
#include <iostream>
#include <algorithm>

#define all(v) v.begin(), v.end()

#define ll long long
#define vi vector<int>
#define vb vector<bool>

using namespace std;

int main() {

    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int t;

    cin >> t;

    while(t--){
        ll n;
        ll x;
        cin >> n >> x;
        if (n % x != 0){
            cout << "-1\n";
            continue;
        }   

        vi pf;

        // init bool vector of size n+1 - default is false
        vb is(n+1, false);
        vi nextVal(n+1);

        // first step is to get all the prime factors of n
        ll v = n / x;
        while (v > 1){  
            for (ll i =2; i <= v; i++){

                // while it is still a prime factor check it
                while (v % i == 0){
                    pf.push_back(i);
                    v = v / i;
                }
            }
        }

        ll cur = x;
        for(auto it:pf){
            is[cur] = true;
            nextVal[cur] = cur * it;
            cur = cur * it;
        }

        for(int i = 1; i <= n; i++ ){
            if(i==1){
                cout << x << " ";
            } 
            else if (i == n){
                cout << 1 << " ";
            }
            else if (is[i]){
                cout << nextVal[i] << " ";
            }
            else {
                cout << i << " ";
            }
        }
        cout << "\n";
    }

    return 0;
}


