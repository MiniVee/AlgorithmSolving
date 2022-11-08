
def groupThePeople(groupSizes):
    answer = []
    dict_size = dict()

    for key, value in enumerate(groupSizes):
        ans = dict_size.get(value, [])
        ans.append(key)
        dict_size[value] = ans

    for key, value in dict_size.items():
        ans2 = []
        for i in value:
            ans2.append(i)
            if len(ans2) == key:
                answer.append(ans2)
                ans2 = []
    return answer



print(groupThePeople([3,3,3,3,3,1,3]))

