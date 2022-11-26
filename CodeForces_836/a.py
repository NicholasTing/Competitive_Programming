t = int(input())

while t!=0:
    w = input()
    w = w + w[::-1]
    print(w)
    t-= 1