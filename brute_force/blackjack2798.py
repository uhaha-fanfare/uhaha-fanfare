N, M = map(int, input().split(' '))
input_numbers = list(map(int, input().split(' ')))
sum = now_max = 0
maxprint = out1 = out2 = False
for i in range(N):
    if (out1):
        maxprint = True
        break
    for j in range(i+1,N):
        if (out2):
            out1 = True
            break
        for k in range(j+1,N):
            sum = input_numbers[i] + input_numbers[j] + input_numbers[k]
            if sum > M:
                continue
            elif sum < M:
                
                if now_max < sum:
                    # print(now_max, sum)
                    # print(i, j, k)
                    now_max = sum
            else:
                out2 = True
                break
        
if maxprint:
    print(M)
else:
    print(now_max)