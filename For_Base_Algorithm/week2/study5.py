#시작 숫자와 공차 입력하면 10개의 숫자가 출력
while True:
    ans1 = int(input("입력: "))
    ans2 = int(input("입력: "))

    for i in range(0, 10):
        print(ans1+(i*ans2))