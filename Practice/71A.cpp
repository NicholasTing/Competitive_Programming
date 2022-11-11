#include <bits/stdc++.h>
#include <iostream>

using namespace std;

// Problem - https://codeforces.com/problemset/problem/71/A
// 800 Rated

int main() {

    std::ios_base::sync_with_stdio(false);
    int t;
    int total_size;
    string word;

    cin >> t;
    
    while(t--){
        cin >> word;
        total_size = word.size();
        if (total_size > 10) {
            cout << word.at(0) << total_size - 2 << word.at(total_size-1) << "\n";
        } else {
            cout << word << "\n";
        }
    }

    return 0;
}

