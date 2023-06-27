print('Введите число элементов множества N: ')
n=int(input())
nList=[]
for i in range(n):
    print('введите ',i+1,'-й элемент множества')
    number = int(input())
    nList.append(number)
print(nList)

print('Введите число элементов множества М: ')
m=int(input())
mList = []
for i in range(m):
    print('введите ',i+1,'-й элемент множества')
    number = int(input())
    mList.append(number)
   
print(mList)
nSet=set(nList)
mSet=set(mList)
iSet=nSet.intersection(mSet)
print(iSet)
iList=list(iSet)
iList.sort()
print(iList)