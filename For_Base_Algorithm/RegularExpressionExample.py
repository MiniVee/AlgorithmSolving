import re

def solution(strs):
    string = "(AAB+|BAB+A)+"
    pattern = re.compile(string)

    count = 0

    for i in range(len(strs)):
        a = strs[i]
        m = pattern.fullmatch(a)

        if m:
            count +=1

    return count

print(solution(["AABAAA", "BABABB", "BABBAAAB", "BABAAABAABBABBA"]))
