# https://swexpertacademy.com/main/code/problem/problemDetail.do

T = int(input())
game = []
for i in range(1, T+1):
    i = str(i)
    count = 0
    for j in i:
        if j == "3" or j == "6" or j == "9":
            count +=1

    if count == 0:
        game.append(i)

    else:
        game.append(count * "-")

print(" ".join(game))
# 10
# 1 2 - 4 5 - 7 8 - 10

