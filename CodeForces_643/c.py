A , B, C, D = map(int,input().split())

total_len = A + B + C

lens = [A,B,C]

def findnumberofTriangles(A,B,C,D): 

    count = 0
    seen = []
    ans = []
    if A == B and A == D:
        count += 1
    for i in range(A, B+1): 

        for j in range(B, C+1): 

            for k in range(C,D):
                if (i,j,k) in seen:
                    continue

                if i + j > k and j + k > i and i + k > j:
                    count += 1
                    ans.append((i,j,k))
                        
                seen.append((i,j,k))
    
    print(ans)

    return count 

ans = findnumberofTriangles(A,B,C,D)
print(ans)

 


