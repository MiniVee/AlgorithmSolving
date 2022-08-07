# https://school.programmers.co.kr/learn/courses/30/lessons/1845

# 내 풀이
def solution(nums):
    answer = 0
    divNums = len(nums) // 2
    sNum = set(nums)

    if len(sNum) > divNums:
        answer += divNums
    else:
        answer = len(sNum)
    return answer

# 다른 풀이
nums = [3,3,3,2,2,2]
nums.sort()
answer = 0
pocketmon = 0
for i in nums:
    if i != pocketmon and answer < len(nums)/2:
        answer += 1
        pocketmon = i

print(answer)
