A,B = map(int, input().split())

if (A == 0)and(B < 45):
    print('23',(60-(45-B)))
elif (A > 0)and(B < 45):
    print((A-1),(60-(45-B)))
else:
    print((A),(B-45))
    
