A, B = map(int, input().split())
cnt = 1
while A < B:
    if B % 10 == 1:
        B //= 10
        cnt += 1
    elif B % 2 == 0:
        B //= 2
        cnt += 1
    else:
        break
if A == B:
    print(cnt)
else:
    print(-1)
