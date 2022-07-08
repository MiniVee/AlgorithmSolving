#문제:3,6,9 게임 만들기 (글자를 무한대로 입력받아서 현재 차례에 맞지않는 내용을 입력하면 게임 종료)

firstList = []

for i in range(1,100):
    if i%10 == 3 or i%10 == 6 or i%10 == 9 or '3' in str(i) or '6' in str(i) or '9' in str(i):
        i = "짝"
    firstList.append(i)
finalList = list(map(str, firstList))


# while True: ##첫시도
#     ans = str(input("입력: "))
#     arList.append(ans)
#     print(arList)
#     print(arList[0:1])
#     if finalList[ans:ans] != arList[ans:ans]:
#         print("땡")
# while True:
arList = []
for j in range(0, 100):
    ans = str(input("입력: "))
    arList.append(ans)
    if finalList[j:j+1] != arList[j:j+1]:
        break
    # break

# num = 1
# stnum = '1'
# while True:
#     ans = input("입력: ")
#     stnum = str(num)
#     if '3' in stnum or '6' in stnum or '9' in stnum:
#         stnum = '짝'
#     num+=1
#
#     if stnum != ans:
#         break