print('Введите 6ти значный номер билета для определиня счастливый ли он')
number = int(input())
firstPart = number//1000
secondPart = number%1000
n1 = 0
n2 = 0
while firstPart>0:
    n1=n1 + firstPart%10
    firstPart = firstPart//10
while secondPart>0:
    n2=n2 + secondPart%10
    secondPart = secondPart//10
if n1==n2:
    print('Билет ', number, 'счастливый')
else :
    print('Better luck next time')