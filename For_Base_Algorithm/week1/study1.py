#문제: List에 숫자 5개 입력

list = [] #List 생성

while True: #list가 5개 될 때 까지 반복
    num = int(input("숫자: ")) # input 입력
    list.append(num) # input 숫자 list에 append
    if len(list) == 5: # list length가 5가 되면 멈추기
        break
print(list)