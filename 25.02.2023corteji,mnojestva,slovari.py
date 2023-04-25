#1
'''
data1 = {'Height': ' 2,06 meters', 'Weight': ' 113 kg', 'Age': ' 38 years'}

data2 = {'Height': ' 1,88 meters', 'Weight': ' 90 kg', 'Age': ' 35 years'}

data3 = {'Height': ' 1,98 meters', 'Weight': ' 98 kg', 'Age': ' 60 years'}

data4 = {'Height': ' 1,93 meters', 'Weight': ' 100 kg', 'Age': ' 41 years'}

data5 = {'Height': ' 1,91 meters', 'Weight': ' 91 kg', 'Age': ' 34 years'}

data6 = {'Height': ' 1,88 meters', 'Weight': ' 83 kg', 'Age': ' 30 years'}

data7 = {'Height': ' 1,16 meters', 'Weight': ' 147 kg', 'Age': ' 51 years'}

data8 = {'Height': ' 2,08 meters', 'Weight': ' 109 kg', 'Age': ' 34 years'}

dictionaryNames = {'Леброн Джеймс': data1, 'Стефен Карри': data2, 'Майкл Джордан': data3, 'Дуэйн Уэйд': data4,
                   'Рассел Уэстбрук': data5, 'Кайри Ирвинг': data6, "Шакил О'Нил": data7, 'Кевин Дюрант': data8}


def funk_add():
    name = str(input("Имя"))

    height = float(input("Height"))

    data = {'Height': height}

    dictionaryNames.update({name: data})

    print(dictionaryNames)


def funk_delete():
    print('Что вы хотите удалить: 0 - все данные, 1 - часть данных')

    answer = int(input('Выберите действие: '))

    if answer == 0:
        name = str(input('Имя: '))

        dictionaryNames.pop(name)

    print(dictionaryNames)

    if answer == 1:

        name = str(input('Имя: '))

        count = 0

        for key in dictionaryNames[name]:
            count += 1

            print(count, ' - ', key, ' - ', dictionaryNames[name][key])

        index = int(input('Значение которое хотите удалить : '))

        key = ''

        count = 0

        for i in dictionaryNames[name]:

            count += 1

            if count == index: key = i

        dictionaryNames[name].pop(key)

        print(dictionaryNames)


list = ['Height', 'Weight', 'Age'];


def funk_edit():
    print(dictionaryNames)

    print('Что вы хотите изменить: 0 - все данные, 1 - часть данных')

    answer = int(input('Выберите действие: '))

    if answer == 0:

        old_name = str(input('Старое Имя: '))

        new_name = str(input('Новое Имя: '))

        data = {}

        for item in list:
            value = float(input(item + ' : '))

            data.update({item: value})

        dictionaryNames.pop(old_name)

        dictionaryNames.update({new_name: data})

    if answer == 1:

        name = str(input('Имя: '))

        count = 0

        for key in dictionaryNames[name]:
            count += 1

            print(count, ' - ', key, ' - ', dictionaryNames[name][key])

        index = int(input('Значение которое хотите изменить : '))

        value = int(input('Введите новое значение : '))

        key = ''

        count = 0

        for iKey in dictionaryNames[name]:

            count += 1

            if count == index:
                key = iKey

        dictionaryNames[name].update({key: value})

        print(dictionaryNames)


def funk_find():
    print(dictionaryNames)

    name = (input('Введите имя для поиска : '))

    print(dictionaryNames[name])


def funk_output():
    for player in dictionaryNames:

        print(player, ' - ', end='')

        for item in dictionaryNames[player]:
            print(item, '-', dictionaryNames[player][item], end=' ')

        print()


while True:

    menu = ('Добавить', 'Удалить', 'Изменить', 'Найти', 'Вывести всех баскетболистов')

    count = 0

    print('-------------------------------------------------------------------------------')

    for i in menu:
        count += 1

        print(count, " - ", i)

    print()

    x = int(input('Выберите действие которое вы хотите выполнить: '))

    if x == 1:

        funk_add()

    elif x == 2:

        funk_delete()

    elif x == 3:

        funk_edit()

    elif x == 4:

        funk_find()

    elif x == 5:

        funk_output()

    else:

        break
'''
#2
'''
e2f = {
    'dog': 'chien',
    'cat': 'chat',
    'walrus': 'morse'
}

print(e2f)
print(e2f['walrus'])
'''
#3

#4
class Book:

 def __init__(self, title, author=None, year=None):
  self.title = title
  self.author = author
  self.year = year

book = Book('Title','Author', 2020)

book = Book('Title','Author')
library.add_book(book)

books = library.filter(title='Title')
books = books[0]
library.delete_book(book)

book = Book('Title', 'Author', 2020)
book.display()
book_1 = Book('Чистый код', 'Дядя Боб', 2017)
book_2 = Book('От 2 до 5', 'Корней Чуковский', 1958)
book_3 = Book('Идеальный программист', 'Дядя Боб', 2018)
book_4 = Book('Рецепты татарской кухни', year=2018)

library = Library('Библиотека')
library.add_book(book_1)
library.add_book(book_2)
library.add_book(book_3)
library.add_book(book_4)

print(library.name)
library.list()