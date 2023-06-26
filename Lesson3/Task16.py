import random
print('Введите количество элементов в массиве(будет заполнен случайными числами от 1 до 100)')
count = int(input()) 
numbersList = []
while count>0:
    numbersList.append(random.randint(1,100))
    count=count-1
print(numbersList)
print('Введите число для нахождения количества его повторений в массиве')
number = int(input())
print('количество повторений ', numbersList.count(number))