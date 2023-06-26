import random
print('Введите количество подбрасываемых монеток')
coinsCount = int(input())
coinList = []
while coinsCount>0:
    coinList.append(random.randint(0,1))
    coinsCount=coinsCount-1
print(coinList)
print('Чтобы все монетки были на одной стороне нужно перевернуть')
print(coinList.count(0) if coinList.count(0) < coinList.count(1) else coinList.count(1), 'монеток(-и)')
