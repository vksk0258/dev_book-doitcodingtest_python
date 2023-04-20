import sys
input = sys.stdin.readline

N,L = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(1,N+1):
    s = i - L
    if s < 0:
        s = 0
    print(min(arr[s:i]), end=' ')