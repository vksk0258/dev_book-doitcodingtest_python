import sys
input = sys.stdin.readline

num = int(input())
sum = int(input())
a = list(map(int,input().split()))
a.sort()
i = 0
j = num - 1
res = 0

while i < j:
    if a[i] + a[j] < sum:
        i += 1
    elif a[i] + a[j] > sum:
        j -= 1
    else:
        res += 1
        i += 1
        j -= 1
        
print(res)
