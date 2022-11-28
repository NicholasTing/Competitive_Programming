#include <vector>
#include <iostream>
#include <algorithm>

#define ll long long 
#define all(v) v.begin(), v.end()

using namespace std;

int main() {

    std::ios_base::sync_with_stdio(false);
    int t;

    cin >> t;
    ll ans = 1000000;
    while(t--){
        ll n;
        cin >> n;
        ll total = ans / n;
        cout << total << "\n";
        
    }

    return 0;
}


