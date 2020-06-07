T = int(input())


while T != 0:
    T -= 1
    n = int(input())
    if n == 1:
        print('1')
    
    elif n == 2 :
        print('1 2')

    else:

        if n  % 2 == 0:
            fa = [0] * n
            middle = int((n / 2)) - 1
            total = n
            count = 1
            alternate = True
            prev_middle = middle
            
            while middle != 0:
                fa[middle] = count
                if alternate:
                    if n % 2 == 0:
                        middle = (prev_middle + 1) + int(n / 2)
                    else:
                        middle =  (middle + 1) + int
                count += 1

        elif n % 2 == 1:
            first_half = int(n/2)
            second_half = int(n/2)
            fh = []
            sh = [1]
            i = 1
            while i <= first_half:
                sh.append(2*i+1)
                fh.append(2*i)
                i += 1
            
            fa = fh + sh
            print(' '.join([str(e) for e in fa]))
            
