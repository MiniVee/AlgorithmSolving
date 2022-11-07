# https://school.programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    answer = []
    exist = []
    cnt = 0
    for i in range(len(words)):
        if len(exist) == 0:
            exist.append(words[0])
            continue
        else:
            exist.append(words[i])
            if exist[i-1][-1] != exist[i][0]:
                print(exist[i])
                human = n//i
                whatNum = n%i
            if exist.count(exist[i]) == 2:
                print(exist[i])

    #print(exist)
    
    return answer

#print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
#print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))