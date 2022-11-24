#include <vector>
#include <iostream>
#include <algorithm>
#include <map>

#define ll long long

using namespace std;

int main()
{

    std::ios_base::sync_with_stdio(false);
    int t;

    cin >> t;

    while (t--)
    {

        ll n;
        cin >> n;
        vector<ll> a;
        a.clear();

        ll x;
        for (ll i = 0; i < n; i++){
            cin >> x;
            // a.back() returns the last element of the array
            if (i == 0 || x != a.back()){
                a.push_back(x);
            }
        }

        if (a.size() == 1){
            cout << "YES\n";
        }
        else{
            // numValleys
            ll nV = 0;
            bool valid = false;
            for (ll i = 0; i < a.size(); i++)
            {
                if( (i == 0 or a[i-1]  > a[i]) and (i == (a.size() - 1) or a[i] < a[i+1] )) {
                    nV++;
                }
            }

            if(nV == 1){
                cout << "YES\n";
            }
            else{
                cout << "NO\n";
            }
        }
    }

    return 0;
}
