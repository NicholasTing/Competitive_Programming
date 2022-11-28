#include <vector>
#include <iostream>
#include <algorithm>
#include <map>

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
        a.clear();

        ll num1 = 0;
        ll num0 = 0;

        ll n1;

        for (ll i = 0; i < n; i++){
            cin >> n1;
            a.push_back(n1);
            num1= num1 + n1;
        } 

        cout << "total num 1 is " << num1 << "\n";

        cout << "total num 0 is " << n - num1 << "\n";

        cout << "\n";
    }

    return 0;
}


