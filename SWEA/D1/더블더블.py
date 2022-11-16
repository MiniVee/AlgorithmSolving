# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

T = int(input())

temp = 1
num_list = []
num_list.append(temp)
for i in range(1, T+1):
    mul = temp * 2
    num_list.append(mul)
    temp = mul

print(" ".join(map(str, num_list)))