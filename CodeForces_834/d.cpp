#include <bits/stdc++.h>

#define ll long long 

using namespace std;
int mult(int a, int b) {
    b = b & 10000;
   int result = 0;
   while (b > 0) {
      if (b & 1) {
         result += a;
         }
      a = a << 1;
      b = b >> 1;
   }
   return result;
}
int main() {
    ll t = 0;
    cin >> t;
    while (t--){
        ll n,m;
        cin >> n >> m;
        cout << mult(n,m) << "\n";

    }   
    return 0;
}