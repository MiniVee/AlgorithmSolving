
def solution(prices, coupons):
    answer = []
    for i in range(len(prices)):
        for j in range(len(coupons)):
            if coupons[j] == 0:
                continue
            if i > j:
                coupons[j] = 999999
                continue
            if coupons[j] < 0:
                coupons[j] = 999999
                continue
            if prices[i] >= coupons[j] and i <= j:
                sale = prices[i] - coupons[j]
                answer.append(sale)
                coupons[j] = 999999
                break
        else:
            answer.append(prices[i])

    return answer


print(solution([8, 3, 5, 9, 2],
               [4, 2, 4, 8, 1]))

print(solution([8, 3, 5, 9, 2],
               [4, -4, 2, 4, 6]))

print(solution([4, 2, 5, 9, 2],
               [5, 6, 1]))

print(solution([8, 3, 5],
               [4, 4, 7, 4, 6]))