T = int(input())

while T != 0:
    n,k = map(int,input().split())
    count = 2
    final_ans = n
    while k != 0:
        count = 2
        while count < n:
            if final_ans % count == 0:
                final_ans = final_ans + count
                break
            count += 1

        if count == n:
            final_ans = final_ans + n
        if count == 2:
            final_ans = final_ans + (k-1) * 2
            break

        k -= 1

    print(final_ans)

    T -= 1