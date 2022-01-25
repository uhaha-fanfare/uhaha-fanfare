N = int(input())
max = 0
# idx = [0 for i in range(10000)]
idx = []
for i in range(N):
    t = int(input())
    idx[t-1] += 1;
    if max < t:
        max = t
for t in range(max):
    for i in range(idx[t]):
        print(t+1)