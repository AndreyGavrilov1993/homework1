import pickle
import json

### Задание 1

class Car:
    def __init__(self, mark):
        self.mark = mark
        self.age = 15

    def vrym_vrym(self):
        print("vrym_vrym" + self.mark)

    def save_car(self):
        return pickle.dumps(self)

    def save_car_class(self):
        return pickle.dumps(self.__class__)

    def save_car_json(self):
        with open("car.json", "w", encoding="utf-8") as f:
            f.write(json.dumps(self.__dict__, indent=4))

    def __str__(self):
        return self.mark

car = Car("car_1")
car.save_car()

### Задание 2

class Book:
    def __init__(self, mark):
        self.mark = mark
        self.age = 20

    def read_read(self):
        print("read_read" + self.mark)

    def save_book(self):
        return pickle.dumps(self)

    def save_book_class(self):
        return pickle.dumps(self.__class__)

    def save_book_json(self):
        with open("book.json", "w", encoding="utf-8") as f:
            f.write(json.dumps(self.__dict__, indent=4))

    def __str__(self):
        return self.mark

book = Book("book_1")
book.save_book()

### Задание 3

class Stadium:
    def __init__(self, mark):
        self.mark = mark
        self.age = 30

    def holding_a_competition(self):
        print("holding_a_competition" + self.mark)

    def save_stadium(self):
        return pickle.dumps(self)

    def save_stadium_class(self):
        return pickle.dumps(self.__class__)

    def save_stadium_json(self):
        with open("stadium.json", "w", encoding="utf-8") as f:
            f.write(json.dumps(self.__dict__, indent=4))

    def __str__(self):
        return self.mark

stadium = Stadium("stadium_1")
stadium.save_stadium()