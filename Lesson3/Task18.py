import random
print('Введите количество элементов в массиве(будет заполнен случайными числами от 1 до 100)')
count = int(input()) 
numbersList = []
while count>0:
    numbersList.append(random.randint(1,100))
    count=count-1
print(numbersList)
numbersList.sort()
print('Введите число для поиска ближайшего элемента по значению')
number = int(input()) 
for i in range(len(numbersList)):
    if numbersList[i]>number:
        minN=numbersList[i-1]
        maxN=numbersList[i]
        print(minN if number-minN<maxN-number else maxN)
        break
