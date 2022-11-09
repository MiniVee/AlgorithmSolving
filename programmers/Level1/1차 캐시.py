def solution(cacheSize, cities):
    answer = 0
    cachehit = 1
    cachemiss = 5
    cnt = 0
    res = []
    for i in range(len(cities)):
        res.append(cities[i])

        if len(res) > cacheSize:
            if res[0] == cities[i]:
                answer += cachehit
                res.pop(0)
            else:
                answer += cachemiss
                res.pop(0)
        answer += cachemiss

    return answer

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))