import random
print('Введите количество кустов на грядке')
bushCount = int(input())
bushList = []
while bushCount>0:
    bushList.append(random.randint(1,9))
    bushCount=bushCount-1
print(bushList)
minBerries = 3
i=-1
for i in range (len(bushList)):
    if (bushList[i]+bushList[i-2]+bushList[i-1] > minBerries):
        minBerries = bushList[i]+bushList[i-2]+bushList[i-1]
print(minBerries)