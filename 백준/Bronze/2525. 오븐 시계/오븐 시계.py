A, B = map(int, input().split())
C = int(input())

D = B + C

if D >= 60:
    A += (D) // 60
    if A > 23:
        A -= 24
    D %= 60

print(A, D)