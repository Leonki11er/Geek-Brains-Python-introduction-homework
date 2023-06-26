print('Введите сначала сумму затем произведение задуманных чисел')
sum = int(input())
product = int(input())
for i in range(1, sum + 1):
        for j in range(1, sum + 1):
            if i + j == sum and i * j == product:
                firstNumber = i
                secondNumber = j
print('первое задуманное число ',firstNumber,'второе задуманное число ',secondNumber)