myMoney = 1260

money = [500, 100, 50, 10]
count = 0

for m in money:
    count += myMoney // m
    myMoney = myMoney % m

print(count)