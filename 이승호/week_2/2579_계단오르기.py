N = int(input())
stair = [int(input()) for _ in range(N)]
score = [0] * (N)
score[0] = stair[0]
score[1] = stair[1] + stair[0]
score[2] = max(stair[2] + stair[1], stair[2] + stair[0])
max_score = 0

for x in range(3, N):
    if x > 2:
        score[x] =  max(stair[x] + score[x-2], stair[x] + stair[x-1] + score[x-3])

print(score[N-1])


'''
6
10
20
15
25
10
20
'''