#K가 홀수이면 3번부터, 짝수이면 2번부터
one = []
K = int(input())
for i in range(1,K+1):
    one.append(i)
two = []
three = []
base = [one,two,three]
trace = []

def replace(atob):
    a = int(atob[0])-1
    b = int(atob[2])-1
    base[b].insert(0, base[a][0])
    del base[a][0]
    trace.append(atob)

print(base)

input_data = input()
while input_data != '-1':
    replace(input_data)
    print(base)
    input_data = input()