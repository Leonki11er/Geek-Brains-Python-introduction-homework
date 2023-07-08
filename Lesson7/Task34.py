song = 'кто-ходит-в-гости-по-утрам тот-поступает-мудро'
def rhythm_check(crambo_line):
    phrases = crambo_line.split()

    sum_list = [sum(i in 'уеыаоэяию' for i in phrase) for phrase in phrases]
 
    if len(set(sum_list)) == 1 :
        return "Парам пам-пам"  
    else: return "Пам парам"
 
print(rhythm_check(song))