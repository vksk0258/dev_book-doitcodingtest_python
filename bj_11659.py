# data_in = list(map(int,input().split()))
# data_list = list(map(int,input().split()))

# result_list=[]

# for i in range(data_in[1]):
#     data_sector = list(map(int,input().split()))
#     result_list.append(sum(data_list[data_sector[0]-1:data_sector[1]]))
#     print(result_list[i])

import sys
input = sys.stdin.readline
suNo, quizNo = map(int,input().split())
data_list = list(map(int,input().split()))

result_list=[0]
temp = 0

for i in data_list:
    temp = temp + i
    result_list.append(temp)

    
for i in range(quizNo):
    s, e = map(int,input().split())
    print(result_list[e]-result_list[s-1])
    