# https://school.programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    answer = 0
    dict_s = {0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5: "five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
    for key, value in dict_s.items():
        s = s.replace(value, str(key))
        answer = s
    return int(answer)

print(solution("one4seveneight"))
print(solution("2three45sixseven"))