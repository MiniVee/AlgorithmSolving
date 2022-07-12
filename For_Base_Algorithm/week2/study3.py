#문제: 한 개의 값으 ㄹ입력 받아 1부터 그 사이의 모든 숫자를 거꾸로 출력
while True:
    ans = int(input("입력: "))
    for i in range(ans, 0, -1):
        if ans > 1:
            print(i)
        else:
            print("잘못 입력하셨습니다.")