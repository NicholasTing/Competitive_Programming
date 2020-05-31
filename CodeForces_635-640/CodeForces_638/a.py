T = int(input())


number_of_twos = []
for i in range(1,31):
    number_of_twos.append(2**i)

count = 0
for i in number_of_twos:
    count += 1


answer = 0
while T != 0:
    n = int(input())
    first_half = []
    fh_c =0
    sh_c = n
    second_half = []
    # if n == 2:
    #     print('2')
    #     T -= 1
    #     continue

    # else:
    half = int(n/2)
    half2 = half
    first_half.append(number_of_twos[n-1])
    while half != n:
        second_half.append(number_of_twos[half-1])
        half +=1  
    
    while fh_c != half2-1:
        first_half.append(number_of_twos[fh_c])
        fh_c += 1

    print(sum(first_half)-sum(second_half))

    T -= 1