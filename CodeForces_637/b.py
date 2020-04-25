T = int(input())

while T != 0:
    n , k = map(int,input().split())
    numbers = list(map(int,input().split()))
    # [l, l+k-1]
    peaks = [0]
    for i in range(1, len(numbers)-1):
        if numbers[i] > numbers[i-1] and numbers[i] > numbers[i+1]:
            peaks.append(1)
        else:
            peaks.append(0)
    peaks.append(0)
    
    best_l = 0

    current_peaks = 0
    best_peaks = 0

    for i in range(n-k+1):

        current_peaks = sum(peaks[i:i+k-1])
        # print(peaks)
        # print(peaks[i:i+k])

        if current_peaks > best_peaks:
            # print('best peak found')
            # print(best_l)
            best_l = i
            best_peaks = current_peaks

    
    maximum_breaks = best_peaks + 1

    print('%d %d' % (maximum_breaks,best_l+1))

    T -= 1
