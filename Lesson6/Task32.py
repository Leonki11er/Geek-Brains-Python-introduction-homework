from random import randint


count = int(input('Введите количество элементов в массиве(будет заполнен случайными числами от 1 до 100): ')) 
number_list = []
while count > 0:
    number_list.append(randint(1, 100))
    count = count - 1
print(number_list)

min_border = int(input('Введите минимум поиска: '))
max_border = int(input('Введите максимум поиска: '))
index_list = []
for i in range(len(number_list)):
    if min_border <= number_list[i] <= max_border:
        index_list.append(i)
print(index_list)
