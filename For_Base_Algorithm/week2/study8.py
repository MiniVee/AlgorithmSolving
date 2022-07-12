#두 정수를 입력 받고 두 수중에 더 큰 수를 출력, 같으면 두 수 모두 출력

while True:
    ans1 = int(input("입력: "))
    ans2 = int(input("입력: "))
    if ans1 > ans2:
        print(ans1)
    elif ans1 < ans2:
        print(ans2)
    else:
        print(ans1, ans2)