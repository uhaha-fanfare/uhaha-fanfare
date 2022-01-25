N = list(input())
N.sort(reverse = True)
result = ''
for c in N:
    result += c
print(result)