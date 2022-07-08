#문제: 무한반복으로 숫자를 입력 받아 해당 구구단 출력하기(ex, 2를 입력받았으면 2단만 출력, -1을 입력하면 무한 반복 종료)

while True: #무한
    num = int(input("숫자: "))
    if num == -1: # 숫자가 -1이면 멈추기
        break
    for i in range(num, num + 1): # 입력한 숫자의 구구단 배출
        for j in range(1, 10):
            print(i, "x", j, "=", i * j)
