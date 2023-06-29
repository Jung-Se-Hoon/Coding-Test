hour, min = map(int, input().split())
C = int(input())

hour += C // 60
min += C % 60

if min>=60:
    hour += min//60
    min %= 60

if hour >= 24:
    hour -= 24
    
print(hour, min)