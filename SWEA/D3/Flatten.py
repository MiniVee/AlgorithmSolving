

for test_case in range(1, 11):
    dump = int(input())
    box = list(map(int, input().split()))
    for i in range(dump):
        maxBox = max(box)
        minBox = min(box)
        maxBoxIndex = box.index(maxBox)
        minBoxIndex = box.index(minBox)
        box[maxBoxIndex] -= 1
        box[minBoxIndex] += 1
    res = max(box) - min(box)
    print("#",test_case, " ",res, sep="")
