N = int(input())
found = 0
for i in range(1,N):
    S = list(map(int,str(i)))
    decompose = i + sum(S)
    if decompose == N:
        found = i
        break
print(found)