def oper(a,b):
    if len(a)>len(b):
        return True
    else:
        if len(a) == len(b) and a>b:
            return True
        else:
            return False

lis = []
N = int(input())
alreadyexist = False
for i in range(N):
    alreadyexist = False
    t = input()
    for j in lis:
        if j == t:
            alreadyexist = True
            break
    if not alreadyexist:
        lis.append(t)
N = len(lis)

for i in range(N):
    for j in range(1,N-1):
        if oper(lis[j-1],lis[j]):
            lis[j-1],lis[j] = lis[j],lis[j-1]
for i in lis:
    print(i)