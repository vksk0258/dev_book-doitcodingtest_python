# import sys
# input = sys.stdin.readline

# size, count = map(int,input().split())

# two_list = []
# list_sum =[0]
# temp = 0

# for i in range(size):
#     two_list.append(list(map(int,input().split())))
    
# for i in range(size):
#     for j in range(size):
#         temp = temp + two_list[i][j]
#         list_sum.append(temp)
# print(two_list)
# print(list_sum)
        
# for i in range(count):
#     x1,y1,x2,y2 = map(int,input().split())
#     print(list_sum[size*(x2-1)+y2] - list_sum[size*(x1-1)+y1-1])
    

import sys
input = sys.stdin.readline

size, count = map(int,input().split())

o_matrix = [[0]*(size + 1)]
s_matrix = [[0]*(size + 1) for _ in range(size + 1)]


for i in range(count):
    o_row = [0] + list(map(int,input().split()))
    o_matrix.append(o_row)
    
for i in range(1, size + 1):
    for j in range(1, size + 1):
        s_matrix[i][j] = s_matrix[i-1][j] + s_matrix[i][j-1] - s_matrix[i-1][j-1] + o_matrix[i][j]

for _ in range(count):
    x1, y1, x2, y2 = map(int,input().split())
    result = s_matrix[x2][y2] - s_matrix[x1-1][y2] - s_matrix[x2][y1-1] + s_matrix[x1-1][y1-1]
    print(result)