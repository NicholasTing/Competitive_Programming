#include <bits/stdc++.h>

using namespace std;

int MAX = 2001;

void solve() {
    int n,k;
    int ans[MAX];
    int number;
    int count = 0;
    cin >> n >> k;
    int N;
    int size;
    N = n;
    string s;
    while(N--){
        cin >> s;
        size = s.length();
       
        cout << setw(size) << setfill('0') << s << "\n";
        count++;
    }
//    for(int i =0; i<n;i++){
//        cout << ans[i];
//    }

    
}

int main()
{

#ifndef ONLINE_JUDGE
    freopen ("input.txt","r",stdin);
    freopen ("output.txt","w",stdout);
#endif
    
    solve();

}

