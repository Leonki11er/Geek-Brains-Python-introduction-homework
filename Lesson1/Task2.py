print('Введите число для нахождения суммы его цифр')
number = int(input())
n=0
while number>0:
    n=n + number%10
    number = number//10
print(n)