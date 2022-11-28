#include <bits/stdc++.h>
#include <iostream>

#define ll long long 

using namespace std;

int main() {

    std::ios_base::sync_with_stdio(false);
    int t;

    cin >> t;
    
    while(t--){

        int n;
        string s;
        cin >> n >> s;

        ll ans = 0;
        for (int i = 0; i < n; i++){

            // default dict
            vector<int> default_dict (10);

            // different elements
            int de = 0;

            for (int j = i; j < min(i+300, n); j++) {

                auto count = s[j] - '0';

                if (default_dict[count] == 0){
                    de++;
                }

                default_dict[count]++;

                if(*max_element(default_dict.begin(),default_dict.end() ) <= de){
                    ans++;
                }
            }
        }

        cout << ans << "\n";
 
    }

    return 0;
}


