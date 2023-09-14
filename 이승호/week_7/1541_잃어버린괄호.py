p = input()

formula = p.split('-')

ans = []
for i in formula:
    tmp = 0
    f = i.split('+')
    for j in f:
        tmp += int(j)
    ans.append(tmp)
    
result = ans[0]
if len(ans) >= 2:
    for k in range(1, len(ans)):
        result -= ans[k]

print(result)
