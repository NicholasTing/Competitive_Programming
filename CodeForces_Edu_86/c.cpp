#include <bits/stdc++.h>
#include <numeric>

using namespace std;

typedef long long ll;
// (x,y)
typedef pair<int,int> ii;
// vector int
typedef vector<int> vi;
// dict (x,y) = something
typedef vector<ii> vii;
// edgelist
// typedef<pair<int, ii>> EdgeList;

int gcd(int a, int b){
    return b == 0 ? a: gcd(b, a%b);
}

int lcm(int a, int b){
    return (a*b)/gcd(a,b);
}

int main() {

    int T;
    cin >> T;
    while (T--){     
        int a,b,q;
        cin >> a >> b >> q;
        int lc;
        lc = lcm(a,b);
        int ans;
        int x,y;
        while(q--){

            cin >> x >> y;
            ans = 0;
            cout << lc << "\n";
           
            if (lc == b || (lc < y)){
                out << 0 << " ";
                continue;
            }
            cout << ans << " ";
        }
        cout << "\n";
    }   
	
	return 0;
}
