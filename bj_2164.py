from collections import deque
N = int(input())
card_list = deque()

for i in range(N):
    card_list.append(i+1)

for _ in range(N-1):
    card_list.popleft()
    card_list.append(card_list.popleft())
    
print(card_list[0])