T = int(input())
res = []
for test_case in range(1, T + 1):
    num = input()
    nList = list(map(int, num))
    while True:
        cnt = 0
        for i in nList:
            cnt += i
        if cnt >= 10:
            nList = list(map(int, str(cnt)))
        else:
            res.append((test_case, cnt))
            break

for test_case, j in res:
    print(f"#{test_case} {j}")


