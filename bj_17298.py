n = int(input)
ans = [0] * n
A = list(map(int, input().split()))
my_stack = []

for i in range(n):
    while my_stack and A[my_stack[-1]] < A[i]: # 오큰수 조건
        ans[my_stack.pop()] = A[i] # 정답 리스트에 오큰수 저장
    my_stack.append(i)
    
while my_stack:
    ans[my_stack.pop()] = -1
    
result = ""
for i in range(n):
    result += str(ans[i]) + " "
    
print(result)