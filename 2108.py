N = int(input())
numbers = []
count = []
cnt = 0
min = 4000
max = -4000
sum = 0
for i in range(N):
    t = int(input())
    sum += t
    if min > t:
        min = t
    if max < t:
        max = t
    numbers.append(t)
numbers.sort()
for i in range(N-1):
    if numbers[i] == numbers[i+1]:
        cnt += 1
    elif numbers[i] != numbers[i+1]:
        cnt += 1
        count.append([cnt,numbers[i]])
        cnt = 0
if N > 1 and numbers[N-2] == numbers[N-1]:
    count.append([cnt,numbers[N-1]])
elif N > 1 and numbers[i] != numbers[i+1]:
    count.append([1,numbers[i+1]])
count.sort(reverse=True)
print(count)

print('%.0f' % (sum/N))
print(numbers[N//2])
i = 0
tmp = []
while count[i][0] == count[i+1][0]:
    tmp.append(count[i][1])
    i += 1
print()
print(max - min)