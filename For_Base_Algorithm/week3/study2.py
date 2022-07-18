# 문제설명: 자연수가 적힌 2 x N 장의 카드묶음을 가지고 있습니다. 카드묶음에는 같은 숫자가 적힌 카드가 2장씩 포함되어 있었는데,  서로 다른 숫자가 적힌 카드 2장을 잃어버렸습니다.
# 2 x N-2 길이의 카드 배열 card가 매개변수로 주어질 때, 잃어버린 숫자 2개를 배열형태로 return 하도록 solution 함수를 완성해주세요. 반환되는 배열은 오름차순으로 정렬되어 있어야 합니다.
# 제한사항: 배열 card의 길이는 2 이상 100,000 이하입니다. card의 원소는 1 이상 100,000,000,000 이하의 자연수입니다.
# 입출력 예: card = [1,3,2,5,3,1] result = [2,5] / card = [1,2,3,4,4,3,2,5] result = [1,5]

# 내 풀이
def solution(card):
    sortCard = sorted(card)             # 먼저 카드 정렬
    for i in range(1, len(sortCard)):
        ans = []
        # print(sortCard.count(i))
        if sortCard.count(i) == 1:      # card는 무조건 2개씩 짝을 짓고, 2개의 숫자만 짝을 이루지 않기에 count == 1 인것만 몇개인지 센다.
            ans.append(i)               # ans라는 배열에 append해서 그대로 출력하면 끝
            # print(i)
    return ans

# 더 나은 풀이
def solution(card):

    setCardElement = set()                              # set을 사용하여 중복을 없앤 집합을 만든다.
    setCardElementDuplicate = set()

    for cardElement in card:                            # 배열 card 원소마다 for 문을 돈다
        if cardElement in setCardElementDuplicate:      # setCardElementDuplicate에 card의 원소가 있으면 continue
            continue

        checkExist = cardElement in setCardElement      # setCardElement에 기존 card 원소가 있는지 확인한다.
        if checkExist == False:                         # setCardElement에 기존 card 원소가 없으면 setCardElement에 원소 추가
            setCardElement.add(cardElement)
        else:                                           # setCardElement에 기존 card 원소가 있는 경우
            setCardElementDuplicate.add(cardElement)    # setCardElementDuplicate에 card 원소추가
            setCardElement.remove(cardElement)          # setCardElement에 card 원소 제거

    lstCardElement = list(setCardElement)               # set함수는 집합이기에 list로 만든다.
    lstCardElement.sort()                               # 정렬해주면 끝
    return lstCardElement