import sys
input = sys.stdin.readline

N = int(input())
A = []

for i in range(N):
    A.append((int(input()), i))
    
max = 0
sorted_A = sorted(A)

for i in range(N):
    if max < sorted_A[i][1] - A[i][1]:
        max = sorted_A[i][1] - A[i][1]
        
print(max+1)