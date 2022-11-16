# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

T = int(input())

for test_case in range(1, T + 1):
    money = input()
    a = 50000
    b = 10000
    c = 5000
    d = 1000
    e = 500
    f = 100
    g = 50
    h = 10
    for i in range(8):
        use1 = int(money) // a
        change1 = int(money) % a
        use2 = change1 // b
        change2 = change1 % b
        use3 = change2 // c
        change3 = change2 % c
        use4 = change3 // d
        change4 = change3 % d
        use5 = change4 // e
        change5 = change4 % e
        use6 = change5 // f
        change6 = change5 % f
        use7 = change6 // g
        change7 = change6 % g
        use8 = change7 // h
        change8 = change7 % h

    print("#" + str(test_case) + "\n" + str(use1) + " " + str(use2) + " " + str(use3) + " " + str(use4) + " " + str(use5) + " " + str(use6) + " " + str(use7) + " " +str(use8))
