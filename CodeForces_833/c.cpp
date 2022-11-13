#include <bits/stdc++.h>
#include <iostream>

using namespace std;
typedef long long ll;

// NOTE:
// This is my attempt of trying to understand the code, if anyone find any
// flaw in this please let me know, am keen to understand how this works.

// Defining the max boundaries of the array as per the problem statement
const ll MAXN=2e5+5;
ll a[MAXN];

// Map to store the frequency of the sum of the subarrays as we iterate over 
// them
map<ll,ll> freq;

void tc(){
    ll n;
    cin>>n;

    // max frequency - most common sum found in the array
    // current sum - current sum of the array
    // answer - total number of subarrays which sum up to 0
    ll maxfr=0,current_sum=0,ans=0;

    // found wildcard - basically when you find 0 
    bool found_wildcard=0;

    // Removing all contents of the frequency map
    freq.clear();

    for(ll i=0;i<n;i++){
        cin>>a[i];

        // If the current element is 0
        if(a[i]==0){

            // If the previous one is 0
            if(found_wildcard) {
                ans+=maxfr;
            }
            else {
                // If we have not found a 0, this is the first time
                // we will add the number of times that 0 occured (either by
                // itself or as a sum of all the numbers)
                ans+=freq[0];
            } 

            // Mark that we have found a wildcard
            found_wildcard=1;
            maxfr=0;
            freq.clear();
        }

        // Whether or not we find a wildcard - add to the current sum this value
        current_sum+=a[i];

        // Max frequency is retrieving the higher of the two values - 
        // the current max 
        // OR 
        // the frequency of the current sum

        // example - if maxfr = 0, freq[0] = 2, the maxfr = 2
        maxfr=max(maxfr,++freq[current_sum]);
    }

    // If we found a wildcard - we will add all the times that we 
    // found 0 as the total sum of the arrays
    if(found_wildcard) { ans+=maxfr; }

    // Otherwise - we will just add the number of time that 0 occured
    else ans+=freq[0];

    cout<<ans<<'\n';
}

int main()
{
    ios_base::sync_with_stdio(false), cin.tie(0);
    ll t; cin>>t; while(t--)
        tc();
    return 0;
}