# while True:
#     ans = int(input("입력: "))
#     if ans == 9999:
#         break
#     for i in range(1, ans+1):
#         for j in range(i):
#             print("*", end='')
#         print()
#

# ans = int(input("입력: "))
# for i in range(1, ans+1):
#     if ans % i == 0:
#         print(i)

while True:
    bCheck = True
    ans = int(input("입력: "))
    for i in range(2, ans):
        if ans % i == 0:
            bCheck = False
            break

    if bCheck == True:
        break