H, M = map(int, input().split())
A = int(input())

H += A // 60
M += A % 60

if M >= 60:
    H +=  M // 60
    M %= 60
    
if H >= 24:
    H -= 24



print(H, M)
