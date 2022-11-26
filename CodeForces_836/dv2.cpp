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
    ll ans = 100000000;
    while(t--){
        ll n;
        cin >> n;

        ll total = (ans) / n;
        // get first and last answer and output
        
        if (n == 2) {
            cout << "1 3\n";
        } 
        else if ((n-2)%2 == 0){
            cout << total + (5000) << " " << total - (5000) << " ";  
            // final answer divided evenly over n numbers evenly
            ll whatsleft = ans - total - total;
            ll i = 1;
            ll addition = (n-2) / n;
            cout <<  "addtest\n" << addition << "test additino\n";
            while (i < n-2){
                cout << total - 5000 + i << " ";
                whatsleft =  whatsleft - 5000 + (total + i);
                i++;
            }
            cout << whatsleft << "\n";
        } else {
            cout << total + (5000) << " " << total - (5000) << " ";  
            ll whatsleft = ans - total - total;
            ll i = 1;
            ll addition = (n-2) / n;
            cout <<  "addtest\n" << addition << "test additino\n";
            while (i < n-2){
                cout << total -5000 + i << " ";
                whatsleft =  whatsleft - 5000 + (total + i);
                i++;
            }
        
            cout <<  whatsleft << "\n";
        }
         
         cout<< "-----next\n";
        
    }
 
    return 0;
}
 