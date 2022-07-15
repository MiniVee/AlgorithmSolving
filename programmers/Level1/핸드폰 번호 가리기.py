# https://school.programmers.co.kr/learn/courses/30/lessons/12948

# 1번 풀이 후
# 리스트로 변환 후 * 을 추가하고 또 마지막 끝번호 추가하고 리스트를 다시 문자열로 변환...
def solution(phone_number):
    list(phone_number)
    print(list(phone_number))
    pnList = []
    for i in range(len(phone_number)-4):
        pnList.append("*")

    ans1 = phone_number[-4:]
    pnList.append(ans1)
    ans2 = "".join(pnList)
    answer = ans2
    return answer

# 2번 풀이 - 더 나은 개선된 풀이
def solution(phone_number):
    return "*" * (len(phone_number) - 4) + phone_number[-4:]