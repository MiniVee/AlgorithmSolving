# https://school.programmers.co.kr/learn/courses/30/lessons/42576

# 내 풀이
def solution(participant, completion):
    answer = ''
    participant = sorted(participant)
    completion = sorted(completion)

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            return answer
    return participant[len(completion)]

# 다른 풀이
import collections
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

part_dict = collections.Counter(participant)
com_dict = collections.Counter(completion)

answer = part_dict - com_dict
print(answer)
print(list(answer))
print(list(answer)[0])

# 다른 풀이
def solution(participant, completion):
    answer = ''
    dict = {}

    for i in participant:
        dict[i] = 1
    for i in participant:
        dict[i] -= 1

    for i in completion:
        dict[i] += 1
    for k, v in dict.items():
        if v != 1:
            answer = k
    return answer

