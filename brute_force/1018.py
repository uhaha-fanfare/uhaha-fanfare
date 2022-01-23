chess1 = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']
chess2 = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']
N, M = map(int,input().split(' '))
input_data = []
for i in range(N):
    input_data.append(input())
min = 64
count = 0
for i in range(N-7):
    for j in range(M-7):
        count = 0
        for a in range(8):
            for b in range(8):
                if chess1[a][b] != input_data[i+a][j+b]:
                    count += 1
        if min > count:
            min = count
        count = 0
        for a in range(8):
            for b in range(8):
                if chess2[a][b] != input_data[i+a][j+b]:
                    count += 1
        if min > count:
            min = count
print(min)