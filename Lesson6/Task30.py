first_element = int(input('Введите первый элемент: '))
difference = int(input('Введите разность: '))
n = int(input('Введите количество элементов: '))
number_list = []
for i in range(n):
    number_list.append(first_element + i * difference)
print(number_list)    