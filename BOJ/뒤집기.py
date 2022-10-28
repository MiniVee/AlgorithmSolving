# https://www.acmicpc.net/problem/1439

S = input()
cntZero = 0
cntOne = 0

if S[0] == "1":
    cntZero +=1
else:
    cntOne += 1

for i in range(len(S) - 1):
    if S[i] != S[i+1]:
        if S[i+1] == "1":
            cntZero +=1
        else:
            cntOne +=1

#print(cntZero, cntOne)
print(min(cntZero, cntOne))





