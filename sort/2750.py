N = int(input())
input_data = []
for i in range(N):
    t = int(input())
    input_data.append(t)
for i in range(N-1):
    for j in range(0, N-1-i):
        if input_data[j] > input_data[j+1]:
            input_data[j], input_data[j+1] = input_data[j+1],input_data[j]

# for i in range(len(input_data)) : 
#     for j in range(len(input_data)) : 
#         print(input_data)
#         if input_data[i] < input_data[j] : 
#             input_data[i], input_data[j] = input_data[j], input_data[i]

# input_data.sort()
for i in input_data:
    print(i)