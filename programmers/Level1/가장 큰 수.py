# https://school.programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    stringNum = list(map(str, numbers))                 # 문자열 리스트로 변환
    stringNum.sort(key=lambda x: x * 4, reverse=True)   # 람다식을 써서 4자리수까지 비교하여 큰 순서대로 나열
    answer = str(int("".join(stringNum)))               # int로 바꿔줘서 "0000"이 "0"이 될 수 있게 만들고 str을 통해 문자열로 바꿔주기

    return answer