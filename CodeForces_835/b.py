t=int(input())

while t != 0:
    l = int(input())
    word = input()

    highest = 0
    word_char = [ord(char) - 96 for char in word]

    print(max(word_char))

    t-=1