#1
import string
import re
s = re.sub(r'\s+', '', re.sub(rf'[{string.punctuation}]', '', input())).lower()
print(s == s[::-1])
#2
'''import re
mytext = "В мире горы есть и долины есть,В мире хоры есть и низины есть,В мире море есть и лавины есть,В мире боги есть и богини есть"
listold = mytext.split()
word = ["мире","есть","и"]
for i in range(len(listold)) :
    w = re.sub(r'[^\w\s]','',listold[i].lower())
    if w in word :
            listold[i] = listold[i].upper()
print(' '.join(listold))'''
#3
#Посчитать точки, знаки вопроса и восклицательные знаки
'''s = input("Введите текст: ")
print(sum(s.count(x) for x in ('.!?')))'''