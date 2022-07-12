#문자 하나를 입력받고 영문 소문자인지 확인하는 프로그램 작성

# while True:
#     ans = input("입력: ")
#     print(ans.islower())

while True:
    ans = input("입력: ")
    ans2 = ord(ans)
    if ans2 < 97 or ans2 >123:
        print("False")
    else:
        print("True")