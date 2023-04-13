num = int(input())

score_list = list(map(int,input().split()))

fake_score = sum(score_list)/num/max(score_list)*100

print(fake_score)