cnt = int(input())
arr=[]

for i in range(cnt):
    num = int(input())
    arr.append(num)

arr.sort()
for i in arr:
    print(i)