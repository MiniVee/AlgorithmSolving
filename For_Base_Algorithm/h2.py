client = {}

while True:
    n = int(input('1. 회원가입 2.프로그램 종료'))
    if n == 1:
        id = input('아이디를 입력하세요')
        password = input('비밀번호를 입력하세요.')
        client[id] = password

    elif n == 2:
        print('----------------------------')
        print('아이디   :   비밀번호')
        print('----------------------------')
        for key in client:
            print(key, " : ", client[key])
        break