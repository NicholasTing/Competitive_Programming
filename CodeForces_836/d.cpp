#include <vector>
#include <iostream>
#include <algorithm>

#define ll unsigned long long int
#define all(v) v.begin(), v.end()

using namespace std;

int main() {

    std::ios_base::sync_with_stdio(false);
    int t;

    cin >> t;
    ll base = 1;

    ll ans = 1 00000 0000 00000 0000;

    while(t--){
        ll n;
        cin >> n;
        ll total = ans / n;
        // get first and last answer and output
        if (n == 2) {
            cout << "1 3\n";
        } 
        else if ((n-2)%2 == 0){
            cout << total + 5 0000 0000 << " " << total - 5 0000 0000 << " ";  
            // final answer divided evenly over n numbers evenly
            ll whatsleft = ans - total - total;
            ll i = 1;
            while (i < n-2){
                cout << total + i << " ";
                whatsleft -= (total + i);
                i++;
            }
            cout << whatsleft << "\n";
        } else{
            cout << total + 5 0000 0000 << " " << total - 5 0000 0000 << " ";  
            ll whatsleft = ans - total - total;
            ll i = 1;
            while (i < n-2){
                cout << total + i << " ";
                whatsleft -= (total + i);
                i++;
            }
            cout <<  whatsleft << "\n";
        }
         
        
    }

    return 0;
}


