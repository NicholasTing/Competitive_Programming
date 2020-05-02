T = int(input())

def find_days(arr,curr_val,target):
    curr_val = sum(arr)
    if curr_val == target:
        return arr
    
    # night = grow
    new_arr = []
    for bact in arr:
        bact = bact / 2
        new_arr.append(bact)
        new_arr.append(bact)
    
    return arr

while T != 0:
    target = int(input())
    ans = [1]
    final_ans = find_days(ans,target)

    T -= 1