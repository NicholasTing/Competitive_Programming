import bisect
t = int(input())

pyramid_heights = [2]
pyramid_height = 2
addition = 5
while pyramid_height < 1000000000:
    pyramid_height = pyramid_height + addition
    addition += 3
    pyramid_heights.append(pyramid_height)

while t !=0:
    height = int(input())

    ans = 0
    pos = (bisect.bisect_left(pyramid_heights, height))

    while height >= 0:
        if height == 0:
            break
        if height < pyramid_heights[0]:
            break
        else:
            if height - pyramid_heights[pos] >= 0:
                height = height - pyramid_heights[pos]
                ans += 1
            else:
                pos -= 1

    # print('ans')
    print(ans)

    t -= 1
