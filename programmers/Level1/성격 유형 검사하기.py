def solution(survey, choices):
    answer = ''
    dict_emotion = {"T": 0, "R": 0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}

    for i in range(len(survey)):
        if choices[i]-4 < 0:
            dict_emotion[survey[i][0]] += 4 - choices[i]
        elif choices[i]-4 > 0:
            dict_emotion[survey[i][1]] += choices[i] - 4

    if dict_emotion["R"] >= dict_emotion["T"]:
        answer += "R"
    else:
        answer += "T"

    if dict_emotion["C"] >= dict_emotion["F"]:
        answer += "C"
    else:
        answer += "F"

    if dict_emotion["J"] >= dict_emotion["M"]:
        answer += "J"
    else:
        answer += "M"

    if dict_emotion["A"] >= dict_emotion["N"]:
        answer += "A"
    else:
        answer += "N"

    return answer

print(solution(["TR", "RT", "TR"],	[1, 1, 1] ))

print(solution(["AN", "CF", "MJ", "RT", "NA"],	[5, 3, 2, 7, 5] ))