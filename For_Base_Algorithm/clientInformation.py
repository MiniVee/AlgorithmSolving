# 풀이 1번
def solution(today, terms, privacies):
    answer = []
    res = []
    score = []

    res.append(today.split("."))
    tyear = res[0][0]
    tmon = res[0][1]
    tday = res[0][2]

    for i in range(len(privacies)):
        answer.append(privacies[i][:10].split("."))
        for j in range(len(terms)):
            if privacies[i][11] == terms[j][0]:
                cnt = (28 * int(terms[j][2:])) + int(answer[i][2]) -1
                mon = cnt // 28
                day = cnt % 28
                if day == 0:
                    mon -= 1
                    day = 28

                answer[i][2] = str(day)
                answer[i][1] = str(int(answer[i][1]) + mon)
                if int(answer[i][1]) > 12:
                    answer[i][0] = str(int(answer[i][0]) + int(answer[i][1]) // 12)
                    answer[i][1] = str(int(answer[i][1]) % 12)

    for i in range(len(answer)):
        if answer[i][0] < tyear:
            score.append(i+1)
        else:
            if answer[i][1] < tmon:
                score.append(i+1)
            else:
                if answer[i][2] < tday:
                    score.append(i+1)

    return score

print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))


# 풀이 2번
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):
    answer = []
    termsDict = {}

    for t in terms:
        termItem = t.split(" ")
        termsDict[termItem[0]] = int(termItem[1])
        #print(termItem, termsDict)
    privNumber = 1

    for privac in privacies:
        splitPriv = privac.split(" ")
        privDate = splitPriv[0]
        termKey = splitPriv[1]
        #print(splitPriv)

        privDate = privDate.replace(".", "-")
        #print(privDate)
        datetime_str = privDate + ' 00:00:00'
        #print(datetime_str)

        date_time_obj = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
        #print(date_time_obj)

        today = today.replace(".", "-")
        datetime_str_today = today + ' 00:00:00'
        todayDateTime = datetime.strptime(datetime_str_today, '%Y-%m-%d %H:%M:%S')
        print(todayDateTime)

        date_time_obj = date_time_obj + relativedelta(months=+termsDict[termKey])
        print(date_time_obj)

        if todayDateTime >= date_time_obj:
            answer.append(privNumber)

        privNumber += 1

    return answer

_today = "2022.05.19"
_terms = ['A 6', 'B 12', 'C 3']
_privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
print(solution(_today,_terms,_privacies))