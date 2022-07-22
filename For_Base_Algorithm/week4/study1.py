# arraySlicing = [1,2,3,4,5,6,7,8,9,10]
# ans1 = arraySlicing[:] # 전체 다 불러온다.
# print(ans1) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# ans2 = arraySlicing[3:] #
# print(ans2) # [4, 5, 6, 7, 8, 9, 10]
# ans3 = arraySlicing[:4]
# print(ans3) # [1, 2, 3, 4]
# ans4 = arraySlicing[2:5]
# print(ans4) # [3, 4, 5]
#
#
# strSlicing = "12345678"
# ans5 = strSlicing[:]
# print(ans5) # 12345678
# ans6 = strSlicing[3:]
# print(ans6) # 45678
# ans7 = strSlicing[:4]
# print(ans7) # 1234
# ans8 = strSlicing[2:5]
# print(ans8) # 345

s = "123456"
newstring = "9"
index = 1
s = s[:index] + newstring + s[index+1:]
print(s)

s = [1,2,3,4,5,6]
newList = [9]
index = 1
s = s[:index] + newList + s[index+1:]
print(s)
