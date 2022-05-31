N, M, K = map(int, input('N, M, K 입력: ').split())
numList = list(map(int, input('숫자 입력: ').split()))
numList.sort(reverse=True)

i = 1
sum = numList[0]

while i < M:
    if i % K == 0:
        sum += numList[1]
    else:
        sum += numList[0]
    i += 1
print(sum)
