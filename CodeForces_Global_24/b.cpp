#include <vector>
#include <iostream>
#include <algorithm>
#include <set>

#define all(v) v.begin(), v.end()

#define ll long long
#define vi vector<int>
#define vb vector<bool>

using namespace std;

int main()
{

    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int t;

    cin >> t;

    while (t--)
    {

        ll n;
        cin >> n;
        vi ans;
        int i = 0;

        set<int> finalAns;

        while (n--)
        {
            cin >> i;
            ans.push_back(i);
            finalAns.insert(i);
        }

        int prevLen = -1;

        sort(all(ans));

         for (auto itr : finalAns)
        {
            for (auto itr2 : finalAns)
            {
                if(itr > itr2){
                    finalAns.insert(itr-itr2);
                }
            }         
            
        } 

        cout << finalAns.size() << "\n";
    }

    return 0;
}
