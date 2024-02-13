# Фабричный метод
from enum import Enum
from math import *

class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

    @staticmethod
    def new_cartesian_point(x, y):
        return  Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))

if __name__ == '__main__':
    p = Point(2, 3)
    p2 = Point.new_polar_point(1, 2)
    print(p, p2)

### Паттерн Строитель

class HtmlElement:
    indent_size = 2

    def __init__(self, name = '', text = ''):
        self.text = text
        self.name = name
        self.elements = []

    def __str(self, indent):
        lines = []
        i = ' ' * (indent * self.indent_size)
        lines.append(f'{i}<{self.name}>')

        if self.text:
            i1 = ' ' * ((indent + 1) * self.indent_size)
            lines.append(f'{i1}{self.text}')

        for e in self.elements:
            lines.append(e.__str(indent + 1))

        lines.append(f'{i}</{self.name}>')
        return '\n'.join(lines)

    def __str__(self):
        return self.__str(0)
    @staticmethod
    def create(name):
        return HtmlBuilder(name)
class HtmlBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.__root = HtmlElement(root_name)

    def add_child(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )

    def add_child_fluent(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )
        return self

    def __str__(self):
        return str(self.__root)

builder = HtmlElement.create('ul')
builder.add_child_fluent('li', 'hello')\
    .add_child_fluent('li', 'world')
print('Ordunary builder')
print(builder)

### Соусы

from abc import ABC, abstractmethod
from enum import Enum
from  collections import namedtuple

PastaBase = namedtuple('PastaBase', ['ThickTomatoMince', 'ColorType'])

# Souse Pesto with basil and arugula(green),
# Souse Son Dried Tomato Pesto(red),
# Pasta with chicken in creamy mushroom sause(white)

class PastaThickTomatoMince(Enum):
    HIGHT = "HIGHT"
    MEDIUM = "MEDIUM"

class PastaColorType(Enum):
    GREEN = "GREEN"
    RED = "RED"
    WHITE = "WHITE"

class PastaSauseType(Enum):
    PESTO = "PESTO"
    TOMATO = "TOMATO"
    CHICKENMUSHROOM = "CHICKEN MUSHROOM"

class PastaTopLevelType(Enum):
    BASIl = "BASIL"
    ARUGULA = "ARUGULA"
    SONDRIEDTOMATO = "SON DRIED TOMATO"
    CHICKEN = "CHICKEN"
    MUSHROOM = "CREAMY MUSHROOM SAUSE"

class Pasta:
    def __init__(self, name):
        self.name = name
        self.thick = None
        self.sause = None
        self.topping = []
        self.cooking_time = None # в минутах

    def __str__(self):
        info: str = f"Pasta name: {self.name} \n" \
                    f"thick type: {self.thick.ThickTomatoMince.name} & " \
                    f"{self.thick.ColorType.name} \n" \
                    f"sause type: {self.sause} \n" \
                    f"topping: {[it.name for it in self.topping]} \n" \
                    f"cooking time: {self.cooking_time} minutes"
        return info

class Builder(ABC):
    @abstractmethod
    def prepare_thick(self) -> None: pass
    @abstractmethod
    def add_sause(self) -> None: pass
    @abstractmethod
    def add_topping(self) -> None: pass
    @abstractmethod
    def get_pasta(self) -> Pasta: pass

class PestoPastaBuilder(Builder):

    def __init__(self):
        self.pasta = Pasta("Pesto")
        self.pasta.cooking_time = 50

    def prepare_thick(self) -> None:
        self.pasta.thick = PastaBase(PastaThickTomatoMince.MEDIUM, PastaColorType.GREEN)

    def add_sause(self) -> None:
        self.pasta.sause = PastaSauseType.PESTO

    def add_topping(self) -> None:
        self.pasta.topping.extend(
            [
                it for it in (PastaTopLevelType.BASIl,
                              PastaTopLevelType.ARUGULA)
            ]
        )

    def get_pasta(self) -> Pasta:
        return self.pasta

class TomatoPastaBuilder(Builder):

    def __init__(self):
        self.pasta = Pasta("Tomato")
        self.pasta.cooking_time = 40

    def prepare_thick(self) -> None:
        self.pasta.thick = PastaBase(PastaThickTomatoMince.HIGHT, PastaColorType.RED)

    def add_sause(self) -> None:
        self.pasta.sause = PastaSauseType.TOMATO

    def add_topping(self) -> None:
        self.pasta.topping.extend(
            [
                it for it in (PastaTopLevelType.SONDRIEDTOMATO,)
            ]
        )

    def get_pasta(self) -> Pasta:
        return self.pasta

class ChickenMushroomPastaBuilder(Builder):

    def __init__(self):
        self.pasta = Pasta("CHICKEN MUSHROOM")
        self.pasta.cooking_time = 40

    def prepare_thick(self) -> None:
        self.pasta.thick = PastaBase(PastaThickTomatoMince.MEDIUM, PastaColorType.WHITE)

    def add_sause(self) -> None:
        self.pasta.sause = PastaSauseType.CHICKENMUSHROOM

    def add_topping(self) -> None:
        self.pasta.topping.extend(
            [
                it for it in (PastaTopLevelType.CHICKEN,
                              PastaTopLevelType.MUSHROOM)
            ]
        )

    def get_pasta(self) -> Pasta:
        return self.pasta

class Director:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder: Builder):
        self.builder = builder

    def make_pasta(self):
        if not self.builder:
            raise ValueError("Builder didn't set")
        self.builder.prepare_thick()
        self.builder.add_sause()
        self.builder.add_topping()

if __name__ == '__main__':
    director = Director()
    for it in (PestoPastaBuilder, TomatoPastaBuilder, ChickenMushroomPastaBuilder):
        builder = it()
        director.set_builder(builder)
        director.make_pasta()
        pasta = builder.get_pasta()
        print(pasta)
        print('----------------------------')

### Prototype

import copy

class People:
    __name: str = ''
    __params: dict = {'Вес': 73, 'Рост': 1.76}

    def __init__(self, donor: 'People' = None):
        if donor is not None:
            self.__name = donor.get_name()
            self.__params = copy.deepcopy(donor.get_params())

    def set_name(self, name: str):
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def get_params(self) -> dict:
        return self.__params

    def set_weight(self, new_weight: int):
        self.__params['Вес'] = new_weight

    def clone(self):
        return People(self)

if __name__ == '__main__':
    people_donor: People = People()
    people_donor.set_name('Петя')

    people_clone: People = people_donor.clone()

print('Донор:', people_donor.get_name(), people_donor.get_params())
print('Клон:', people_clone.get_name(), people_clone.get_params())

people_clone.set_weight(70)
people_clone.set_name('Новый Петя')
print()

print('Донор:', people_donor.get_name(), people_donor.get_params())
print('Клон:', people_clone.get_name(), people_clone.get_params())


