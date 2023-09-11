dir = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 
       'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17,
       'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}

alphabet = [0,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

N = int(input())
cleft = [0] * 27
cright = [0] * 27
for _ in range(N):
    p, cl, cr = input().split()
    if cl != '.':
        cleft[dir[p]] = dir[cl]
    if cr != '.':
        cright[dir[p]] = dir[cr]


pre = ''
in_ = ''
post = ''


def preorder(x):
    global pre
    if x:
        pre += alphabet[x]
        preorder(cleft[x])
        preorder(cright[x])


def inorder(x):
    global in_
    if x:
        inorder(cleft[x])
        in_ += alphabet[x]
        inorder(cright[x])


def postorder(x):
    global post
    if x:
        postorder(cleft[x])
        postorder(cright[x])
        post += alphabet[x]

preorder(1)
inorder(1)
postorder(1)

print(pre)
print(in_)
print(post)
