#include <bits/stdc++.h>
#include <iostream>

using namespace std;

// Problem - https://codeforces.com/problemset/problem/1547/A
// 800 Rated

int main() {

    std::ios_base::sync_with_stdio(false);
    int t;

    cin >> t;

    int x1,x2,xf,y1,y2,yf;
    
    while(t--){
        cin >> x1 >> y1;
        cin >> x2 >> y2;
        cin >> xf >> yf;

        int distance = 0;
        if ( x1 == x2 and x2 == xf){
            if ( (y1 < yf and yf < y2) or (y2 < yf and yf < y1) ){
                distance += 2;
            }
        } else if ( y1 == y2 and y2 == yf ) {
            if ( (x1 < xf and xf < x2) or (x2 < xf and xf < x1) ){
                distance =+ 2;
            }
        }

        distance = distance + abs(x1-x2) + abs(y1-y2);

        cout << distance << "\n";

    }

    return 0;
}

