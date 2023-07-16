a, b = list( input().split())

c = int(a[2]) * 100 + int(a[1]) * 10 + int(a[0]) * 1
d = int(b[2]) * 100 + int(b[1]) * 10 + int(b[0]) * 1

if c > d:
    print(c)
else:
    print(d)
