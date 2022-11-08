# https://school.programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    answer = [0, 0]
    exist = []
    exist.append(words[0])
    last_alpha = words[0][-1]
    for i in range(1, len(words)):
        if words[i] not in exist and words[i][0] == last_alpha:
            exist.append(words[i])
            last_alpha = words[i][-1]
        else:
            answer[0] = i%n + 1
            answer[1] = i//n + 1
            break


    return answer

#print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
#print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))