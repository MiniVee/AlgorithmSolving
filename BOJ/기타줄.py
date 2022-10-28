N, M = map(int, input().split())

brand = []
package = []
single = []
cnt = 0
for _ in range(M):
    price = list(map(int, input().split()))
    brand.append(price)

for i in range(len(brand)):
    package.append(brand[i][0])
for i in range(len(brand)):
    single.append(brand[i][1])

package_min = min(package)
single_min = min(single)

if N < 6:
    if package_min > single_min * N:
        cnt += single_min * N
    elif package_min < single_min * N:
        cnt += package_min
    else:
        cnt += package_min
else:
    if N % 6 == 0:
        num1 = (N // 6)
        res = min(package_min * num1, single_min * N)
        cnt += res
    else:
        num2 = (N // 6) + 1
        ex1 = package_min * num2
        ex2 = package_min * (num2 - 1) + single_min * (N-(6 * (num2 - 1)))
        ex3 = single_min * N
        cnt += min(ex1, ex2, ex3)

print(cnt)
