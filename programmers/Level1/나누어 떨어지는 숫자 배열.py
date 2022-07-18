# https://school.programmers.co.kr/learn/courses/30/lessons/12910

# 정답
def solution(arr, divisor):
    answer = []
    ans1 = []
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            print(arr[i])
            ans1.append(arr[i])
            answer = sorted(ans1)
        if len(ans1) == 0:
            answer = [-1]

    return answer

# 오답
# def solution(arr, divisor):
#     answer = []
#     ans1 = []
#     for i in range(len(arr)):
#         if arr[i] % divisor == 0:
#             print(arr[i])
#             ans1.append(arr[i])
#             answer = sorted(ans1)
#             if len(ans1) == 0:
#                 answer = [-1]
#
#     return answer