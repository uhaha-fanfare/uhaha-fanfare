import sys
N = int(input())
lis = []
for i in range(N):
    a, b = map(int,sys.stdin.readline().split(' '))
    lis.append([a,b])
lis.sort()
for i in range(len(lis)):
    print(lis[i][0],lis[i][1])
