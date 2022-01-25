import sys

N = int(sys.stdin.readline())
lis = []
for i in range(N):
    x, y = map(int,sys.stdin.readline().split(' '))
    lis.append([y,x])
lis.sort()
for i in lis:
    print(i[1],i[0])
