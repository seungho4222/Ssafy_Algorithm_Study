N, M = map(int, input().split())
selected = [0] * N
result = []

def perm(i):
    global selected, result
    if i == N:
        temp = []
        for j in range(N):
            temp += [selected[j]]
        return
    
    for k in range(N):
        selected[i] = k+1
        perm(i+1)
        selected[i] = 0
    return temp

print(perm(0))