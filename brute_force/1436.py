N = int(input())
number = 0
count = 665
while number < N:
    count += 1
    if str(count).find("666") != -1:
        number += 1
print(count)