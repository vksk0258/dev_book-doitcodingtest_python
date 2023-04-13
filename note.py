# numbers = [1,1,1,1,3,3,3,3,34,4,4,5,6,7,8,56,54,6,76,]
# counter = {}

# for number in numbers:
#     if number in counter:
#         counter[number] += 1
#     else:
#         counter[number] = 1

# print(counter)

# x = int(input())

# arr =[["*" for j in range(2*x-1)] for i in range(x)]

# for k in range(x):
#     for n in range(2*k+1):
#         arr[k][(2*x-1)//2] = " "
#     print(*arr[k])

# output = ""

# for i in range(1,15):
#     for j in range(14, i, -1):
#         output += " "
#     for k in range(0, 2 * i - 1):
#         output += "*"
#     output += "\n"

# print(output)

# limit = 10000
# i = 1
# sum = 0

# while sum < limit:
#     sum += i
#     i += 1
    
# print(i,sum)

# max_value = 0
# a = 0
# b = 0

# for i in range(1,100):
#     j = 100 - i
    
#     if max_value <= i*j:
#         max_value = i*j
#         a = i
#         b = j
        
# print(a,b,max_value)

# output=[i for i in range(1,100) if "{:b}".format(i).count("0") == 1]
# for i in output:
#     print(i,":","{:b}".format(i))

# list_num = [1,2,3,4,1,2,3,1,4,1,2,3]
# dic_num = {}

# for i in list_num:
#     if i in dic_num:
#         dic_num[i] += 1
#     else:
#         dic_num[i] = 1

# print(len(dic_num))
# print(dic_num)

# text = "qweqweqweqweqwewqeqweqweqweq"
# print(text.count("q"))

# text_list=[]
# text = "qweewqeqweqweqeqqeewwqeqweqweqwee23"
# for i in range((len(text)//3)+1):
#     text_list.append(text[i*3:i*3+3])
# print(text_list)

# data_list = [1,2,[3,4,[5,6,7]],8,9]

# def flatten(data):
#     result_list=[]
#     for items in data:
#         if type(items) == list:
#             result_list += flatten(items)
#         else:
#             result_list.append(items)
#     return result_list

# print(flatten(data_list))

# min_num = 2
# max_num = 10
# total = 100
# memo = {}

# def func(rest,sit):
#     key = str([rest,sit])
    
#     if key in memo:
#         return memo[key]
#     if rest < 0:
#         return 0
#     if rest == 0:
#         return 1
    
#     count = 0
#     for i in range(sit, max_num + 1):
#         count += func(rest - i, i)
        
#     memo[key] = count
    
#     return count

# print(str([1,3]))

books = []