#

T = int(input())
for i in range(1, T + 1):
    hm = list(map(int, input().split()))

    h = hm[0] + hm[2]
    m = hm[1] + hm[3]
    if m >= 60:
        plusH = m // 60
        remainM = m % 60
        h += plusH
        m -= 60
    if h > 12:
        h -= 12
    print("#" + str(i) + " " + str(h) + " " + str(m))

# 3
# 3 17 1 39
# 8 22 5 10
# 6 53 2 12

#1 4 56
#2 1 32
#3 9 5