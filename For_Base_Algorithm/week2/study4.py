#두 개의 값을 입력 받아 그 사이의 숫자를 모두 출력, 두 번째 수는 첫 번째 수보다 큰 수를 입력하기
while True:
    ans1 = int(input("입력: "))
    ans2 = int(input("입력: "))
    if ans1 > ans2:
        print("두번째 입력 값이 더 커야합니다.")
    else:
        for i in range(ans1, ans2+1):
            print(i)