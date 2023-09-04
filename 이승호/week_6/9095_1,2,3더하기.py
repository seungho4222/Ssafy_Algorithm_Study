def f(idx, total):
    global cnt
    if total == N:
        cnt += 1
        return
    if total > N or idx == N:
        return
    for i in range(1, 4):
        f(idx+1, total+i)


T = int(input())
for tc in range(T):
    N = int(input())
    cnt = 0
    f(0,0)
    print(cnt)