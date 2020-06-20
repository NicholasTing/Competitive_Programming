from collections import defaultdict
import sys
T = int(input())

def solve(s):
    t = '123'
    
    if len(t) > len(s):
        return 0

    hashmap = defaultdict(int)
    for ch in t:
        hashmap[ch] += 1
    
    start = 0
    end = 0
    count = len(hashmap)
    mwl = sys.maxsize
    smw = start
    
    while end < len(s):
        ch = s[end]
        if ch in hashmap:
            hashmap[ch] -= 1
            if hashmap[ch] == 0:
                count -= 1
                
        end += 1
        while count == 0:
            ch = s[start]
            if ch in hashmap:
                hashmap[ch] += 1
                if hashmap[ch] > 0:
                    count += 1
                    if mwl > (end - start):
                        mwl = end - start
                        smw = start

            start += 1
    
    if mwl == sys.maxsize:
        return 0
            
    return len(s[smw: smw + mwl])

while T != 0:
    T -= 1
    a = input()
    a = list(a)
    answer = solve(a)
    print(answer)
    