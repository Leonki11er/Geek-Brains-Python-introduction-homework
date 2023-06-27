engLetters = 'qwertyuiopasdfghjklzxcvbnm'
rusLetters = 'йцукенгшщзхъфывапролджэячсмитьбюё'
engPoints = {1:'AEIOULNSTR', 2:'DG', 3:'BCMP', 4:'FHVWY', 5:"K" , 8:'JX', 10:'QZ'}
rusPoints = {1:'АВЕИНОРСТ', 2:'ДКЛМПУ', 3:'БГЁЬЯ', 4:'ЙЫ', 5:'ЖЗХЦЧ', 8:'ШЭЮ', 10:'ФШЪ'}
print('Введите слово на английском или русском языке: ')
word = input()
if word[0].lower() in engLetters:
     sum = 0
     for letter in word:
         for key, value in engPoints.items():
             if letter.upper() in value:
                 sum += key
     print('стоимость введенного английского слова = ',sum)
else:
    if word[0].lower() in rusLetters:
         sum = 0
         for letter in word:
             for key, value in rusPoints.items():
                 if letter.upper() in value:
                     sum += key
         print('стоимость введенного русского слова = ',sum)