# def solve(rates, customers):
#     res = []
#
#     for i in range(len(customers)):
#         answer = []
#         for j in range(len(rates)):
#                 price = []
#                 price.append(rates[j][0])
#                 if rates[j][1] < customers[j][0]:
#                     if rates[j][1] == -1:
#                         price.append(0)
#                     else:
#                         price.append(((customers[j][0] - rates[j][1]) * rates[j][2])* 60)
#
#                 if rates[j][3] < customers[j][1]:
#                     if rates[j][3] == -1:
#                         price.append(0)
#                     else:
#                         price.append(((customers[j][1] - rates[j][3]) * rates[j][4]))
#
#                 if rates[j][5] < customers[j][2]:
#                     if rates[j][5] == -1:
#                         price.append(0)
#                     else:
#                         price.append(((customers[j][2] - rates[j][5]) * rates[j][6]))
#                 answer.append(sum(price))
#         res.append(min(answer))
#
#     result = sum(res)
#     print(result)
#     return result
#
# solve([[19800, 40, 5, 100, 30, -1, 0], [27500, -1, 0, 150, 20, 2000, 25], [100000, -1, 0, -1, 0, -1, 0]],
#          [[70, 160, 9920], [800, 620, 9100], [900, 200, 500]])



def solution(rates, customers):
    res = []

    for i in range(len(customers)):
        answer = []
        j = 0
        while True:
            price = []
            price.append(rates[j][0])
            if rates[j][1] < customers[j][0]:
                if rates[j][1] == -1:
                    price.append(0)
                else:
                    price.append(((customers[j][0] - rates[j][1]) * rates[j][2])* 60)
            if rates[j][3] < customers[j][1]:
                if rates[j][3] == -1:
                    price.append(0)
                else:
                    price.append(((customers[j][1] - rates[j][3]) * rates[j][4]))
            if rates[j][5] < customers[j][2]:
                if rates[j][5] == -1:
                    price.append(0)
                else:
                    price.append(((customers[j][2] - rates[j][5]) * rates[j][6]))
            answer.append(sum(price))
            res.append(min(answer))
            break
        j+=1


    result = sum(res)
    print(result)
    return result

solution([[19800, 40, 5, 100, 30, -1, 0], [27500, -1, 0, 150, 20, 2000, 25], [100000, -1, 0, -1, 0, -1, 0]],
         [[70, 160, 9920], [800, 620, 9100], [900, 200, 500]])