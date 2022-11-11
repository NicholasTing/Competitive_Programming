    #include <bits/stdc++.h>
    #include <iostream>

    using namespace std;

    // Problem - https://codeforces.com/problemset/problem/1311/A
    // 800 Rated

    int main() {

        std::ios_base::sync_with_stdio(false);
        int t;
        int a, b;

        cin >> t;
        
        while(t--){
            cin >> a >> b;

            // if a == b, 0 operations to transform numbers
            if (a == b) {
                cout << 0 << "\n";
            } 
            
            // if a < b, you need at least one operation to get it to the number
            // a + x where x > 0 and x is odd
            // 2 -> 4 - 2
            // 2 -> 5 - 1
            // 3 -> 4 -> 1
            // 3 -> 5 -> 2
            else if (a < b) {
                // if both even or both odd
                if ((a % 2) == (b % 2)){
                    cout << "2\n";
                } else {
                    cout << "1\n";
                }

            } else {
                // 4 -> 2 - 1
                // 5 -> 2 - 2
                // 4 -> 3 -> 2
                // 5 -> 3 -> 1
                // if both even or both odd
                if ((a % 2) == (b % 2)){
                    cout << "1\n";
                } else {
                    cout << "2\n";
                }
            }
        }

        return 0;
    }

