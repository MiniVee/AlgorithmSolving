#문제: 구구단 9단~2단까지 거꾸로 출력

for i in range(9, 0, -1): # 이중 포문 reverse
    for j in range(9, 0, -1):
        print(i, "x", j, "=", i*j)