#include <bits/stdc++.h>

// To SIT - STAR contest 
// I have converted my python code into cpp 
// Learnt it in a few minutes and hope this work
// if it works, it would be super interesting and a great learning experience.

// nums = list(map(int,input().split()))
// count = 0
// lowest_v = [False for i in range(k)] 

// lowest = 0
// seen = []
// fa = [0 for i in range(n)]

// for i in nums:
//     if i not in seen:
//         seen.append(i)
//         lowest_v[i-1] = False
//         fa.append(i)
//     else:
//         while lowest_v[lowest] != True:
//             lowest += 1
    
//         lowest_v[lowest] = False
//         seen.append(lowest+1)
//         fa.append(lowest+1)

using namespace std;

void solve() {

    int n, k;
    cin >> n;
    cin >> k;
    vector<int> nums;
    vector<int> seen;
    vector<bool> lowest_v;
    vector<int> fa;
    int lowest = 0;
    int i;

    while(n--){
        cin >> i;
        nums.push_back(i);
    }
    while (k--){
        lowest_v.push_back(true);
    }

    for(int i: nums){
        if(find(seen.begin(), seen.end(), i) == seen.end()) {
            seen.push_back(i);
            lowest_v[i-1] = false;
            fa.push_back(i);
        } else {
            /* v does not contain x */
            while (!lowest_v[lowest]){
                lowest++;
            }
            lowest_v[lowest] = false;
            seen.push_back(lowest+1);
            fa.push_back(lowest+1);
        }
    }
    
    for (int i : fa){
        cout << i << " ";
    }
    
}

int main(){
    solve();
}


