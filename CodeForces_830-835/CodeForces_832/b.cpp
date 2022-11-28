#include <bits/stdc++.h>
#include <iostream>

#define ll long long

using namespace std;

// Problem - https://codeforces.com/contest/1747/problem/A

int main() {

    std::ios_base::sync_with_stdio(false);
    cout << setprecision(15) << fixed;
    cin.tie(NULL);

    ll t;

    cin >> t;

    vector<ll> nums;
    
    // Solve here
    while(t--){

        ll n;
        cin >> n;
        ll total = n * 3;
        ll left = 1;
        ll right = total-1;
        nums.clear();
        if (n == 1){
            cout << 1 << "\n" << "1 2\n";
        }
        else if (n == 2){
            cout << 1 << "\n" << "2 6\n";
        }
        else {
            
            ll run_number = 0;
            while (left < right){
                run_number ++;
                nums.push_back(left);
                nums.push_back(right);
                right -= 3;
                if (run_number % 2 == 1){
                    left+=2;
                } else {
                    left ++;
                }
            }

            cout << nums.size() / 2 << "\n";
            ll check = 0;
            for (auto &element : nums) {
                check++;
                cout << element << " ";
                if (check % 2 == 0 and check != nums.size()){
                    cout << "\n";
                }
            }
            
            cout << "\n";
        }

    }

    return 0;
}

