a = int(input())

for i in range(1, 2*a):
    if i < a+1:
        print(" " * (a-i) + i * '*' + (i -1) * '*')
    else:
        print(" " * (i-a) + (((2*a -1)-i) * 2 + 1) * '*' )