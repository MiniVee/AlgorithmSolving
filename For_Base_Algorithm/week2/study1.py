#문제: 구구단 2~9단까지 출력해보기

for i in range(2, 10): # 이중 포문
    for j in range(1, 10):
        print(i, "x", j, "=", i*j)