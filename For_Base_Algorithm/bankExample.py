def solve(rates, customers):
    res = []

    for i in range(len(customers)):
        answer = []
        for j in range(len(rates)):
            price = []
            price.append(rates[j][0])
            if rates[j][1] < customers[i][0]:
                if rates[j][1] == -1:
                    price.append(0)
                else:
                    price.append(((customers[i][0] - rates[j][1]) * rates[j][2])* 60)

            if rates[j][3] < customers[i][1]:
                if rates[j][3] == -1:
                    price.append(0)
                else:
                    price.append(((customers[i][1] - rates[j][3]) * rates[j][4]))

            if rates[j][5] < customers[i][2]:
                if rates[j][5] == -1:
                    price.append(0)
                else:
                    price.append(((customers[i][2] - rates[j][5]) * rates[j][6]))
            answer.append(sum(price))
        res.append(min(answer))

    result = sum(res)
    print(result)
    return result

solve([[19800, 40, 5, 100, 30, -1, 0], [27500, -1, 0, 150, 20, 2000, 25], [100000, -1, 0, -1, 0, -1, 0]],
         [[70, 160, 9920], [800, 620, 9100], [900, 200, 500]])

solve([[19800, 40, 5, 100, 30, 1200, 22], [27500, 60, 4, 150, 20, 2000, 25], [39600, 200, 3, 100, 40, 6000, 21], [50000, 200, 3, -1, 0, 6000, 21]],
         [[70, 165, 2020], [42, 110, 1205], [100, 120, 6100], [100, 999, 6100], [80, 130, 3500]])



# def solve(rates, customers):
#     res = []
#
#     for i in range(len(customers)):
#         answer = []
#         for j in range(i, len(rates)):
#             price = []
#             price.append(rates[j][0])
#             if rates[j][1] < customers[j][0]:
#                 if rates[j][1] == -1:
#                     price.append(0)
#                 else:
#                     price.append(((customers[j][0] - rates[j][1]) * rates[j][2])* 60)
#
#             if rates[j][3] < customers[j][1]:
#                 if rates[j][3] == -1:
#                     price.append(0)
#                 else:
#                     price.append(((customers[j][1] - rates[j][3]) * rates[j][4]))
#
#             if rates[j][5] < customers[j][2]:
#                 if rates[j][5] == -1:
#                     price.append(0)
#                 else:
#                     price.append(((customers[j][2] - rates[j][5]) * rates[j][6]))
#             answer.append(sum(price))
#         res.append(min(answer))
#
#     result = sum(res)
#     print(result)
#     return result
#
# solve([[19800, 40, 5, 100, 30, -1, 0], [27500, -1, 0, 150, 20, 2000, 25], [100000, -1, 0, -1, 0, -1, 0]],
#          [[70, 160, 9920], [800, 620, 9100], [900, 200, 500]])