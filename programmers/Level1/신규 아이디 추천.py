# https://school.programmers.co.kr/learn/courses/30/lessons/72410

#중요 내용: re 라이브러리, 특수 문자 제거 방법, 중복 시 해당 값 삭제
import re
def solution(new_id):
    answer = ''
    #step1
    lower_id = new_id.lower()
    #step2
    lower_id = re.sub(r"[^a-zA-Z0-9-_.]","",lower_id)
    lower_id = list(lower_id)
    cnt = 0
    #step3
    for i in range(len(lower_id)):
        if lower_id[i] == "." and cnt == 0:
            cnt +=1
        elif lower_id[i] == "." and cnt >= 1:
            lower_id[i] = ''
            cnt +=1
        elif lower_id[i] != ".":
            cnt = 0
    #step4
    if lower_id[0] == ".":
        lower_id.pop(0)
    lower_id = "".join(lower_id)
    #step5
    lower_id = list(lower_id)
    if len(lower_id) == 0:
        lower_id.append("a")
    lower_id = "".join(lower_id)
    #step6
    lower_id = list(lower_id)
    if len(lower_id) > 15:
        lower_id = lower_id[:15]
    if lower_id[-1] == ".":
        lower_id.pop(-1)
    #step7
    if len(lower_id) < 3:
        while len(lower_id) < 3:
            lower_id.append(lower_id[-1])
    lower_id = "".join(lower_id)

    return lower_id

#print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution(	"z-+.^."))
# print(solution("=.="))
# print(solution("123_.def"))
# print(solution("abcdefghijklmn.p"))