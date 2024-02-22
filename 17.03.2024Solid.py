from abc import ABC, abstractmethod
from enum import Enum
from collections import namedtuple

HotDogBase = namedtuple('HotDogBase', ['Sharpness', 'Bun'])

# Traditional hotdog: bun, suasage, tomato sause, ketchup, mayonnaise, mustard, korean carrots, fried onion, 10 minutes, spicy;
# American hotdog: bun, suasage, mustard, fried onion, pickles, sheese, 10 minutes, sweet;
# Village hotdog: bun, sesame, suasage, mayonnaise, ketchup, mustard, pickles, red onion, 15 minutes, sweet;

class HotDogBun(Enum):
    SESAME = "SESAME"
    WITHOUTSESAME = "WITHOUTSESAME"

class SharpnessType(Enum):
    Spicy = "Spicy"
    Sweet = "Sweet"

class HotDogType(Enum):
    Traditional = "Traditional"
    American = "American"
    Village = "Village"

class HotDogTopLevelType(Enum):
    BUN = "BUN"
    KETCHUP = "KETCHUP"
    MAYONNAISE = "MAYONNAISE"
    MUSTARD = "MUSTARD"
    SUASAGE = "SUASAGE"
    TOMATOSAUSE = "TOMATO SAUSE"
    PICKLES = "PICKLES"
    REDONION = "RED ONION"
    FRIEDONION = "FRIED ONION"
    CHEESE = "CHEESE"
    JALAPENO = "JALAPENO"
    KOREANCARROTS = "KOREAN CARROTS"

class HotDog:
    def __init__(self, name):
        self.name = name
        self.sharpness = None
        self.fastfood = None
        self.topping = []
        self.cooking_time = None # в минутах

    def __str__(self):
        info: str = f"HotDog name: {self.name} \n" \
                    f"sharpness type: {self.sharpness.Sharpness.name} & " \
                    f"{self.sharpness.Bun.name} \n" \
                    f"fastfood type: {self.fastfood} \n" \
                    f"topping: {[it.name for it in self.topping]} \n" \
                    f"cooking time: {self.cooking_time} minutes"
        return info

class DiscountCalculator():
    @abstractmethod
    def get_discounted_price(self):
        pass

class DiscountCalculatorTraditional(DiscountCalculator):
    def __init__(self, cost):
        self.cost = cost

    def get_discounted_price(self):
        return self.cost - (self.cost * 0.10)

class DiscountCalculatorAmerican(DiscountCalculator):
    def __init__(self, cost):
        self.cost = cost

    def get_discounted_price(self):
        return self.cost - (self.cost * 0.15)

class DiscountCalculatorVillage(DiscountCalculator):
    def __init__(self, cost):
        self.cost = cost

    def get_discounted_price(self):
        return self.cost - (self.cost * 0.25)

class Builder(ABC):
    @abstractmethod
    def sharpness_thick(self) -> None: pass
    @abstractmethod
    def add_fastfood(self) -> None: pass
    @abstractmethod
    def add_topping(self) -> None: pass
    @abstractmethod
    def get_hotdog(self) -> HotDog: pass

class TraditionalHotDogBuilder(Builder):

    def __init__(self):
        self.hotdog = HotDog("Traditional hotdog")
        self.hotdog.cooking_time = 10

    def sharpness_thick(self) -> None:
        self.hotdog.sharpness = HotDogBase(SharpnessType.Spicy, HotDogBun.WITHOUTSESAME)

    def add_fastfood(self) -> None:
        self.hotdog.fastfood = HotDogType.Traditional

    def add_topping(self) -> None:
        self.hotdog.topping.extend(
            [
                it for it in (HotDogTopLevelType.BUN,
                              HotDogTopLevelType.SUASAGE,
                              HotDogTopLevelType.TOMATOSAUSE,
                              HotDogTopLevelType.KETCHUP,
                              HotDogTopLevelType.MAYONNAISE,
                              HotDogTopLevelType.MUSTARD,
                              HotDogTopLevelType.KOREANCARROTS,
                              HotDogTopLevelType.FRIEDONION)
            ]
        )

    def get_hotdog(self) -> HotDog:
        return self.hotdog

class AmericanHotDogBuilder(Builder):

    def __init__(self):
        self.hotdog = HotDog("American hotdog")
        self.hotdog.cooking_time = 10

    def sharpness_thick(self) -> None:
        self.hotdog.sharpness = HotDogBase(SharpnessType.Sweet, HotDogBun.WITHOUTSESAME)

    def add_fastfood(self) -> None:
        self.hotdog.fastfood = HotDogType.American

    def add_topping(self) -> None:
        self.hotdog.topping.extend(
            [
                it for it in (HotDogTopLevelType.BUN,
                              HotDogTopLevelType.SUASAGE,
                              HotDogTopLevelType.MUSTARD,
                              HotDogTopLevelType.FRIEDONION,
                              HotDogTopLevelType.PICKLES,
                              HotDogTopLevelType.CHEESE)
            ]
        )

    def get_hotdog(self) -> HotDog:
        return self.hotdog

class VillageHotDogBuilder(Builder):

    def __init__(self):
        self.hotdog = HotDog("Village hotdog")
        self.hotdog.cooking_time = 15

    def sharpness_thick(self) -> None:
        self.hotdog.sharpness = HotDogBase(SharpnessType.Sweet, HotDogBun.SESAME)

    def add_fastfood(self) -> None:
        self.hotdog.fastfood = HotDogType.Village

    def add_topping(self) -> None:
        self.hotdog.topping.extend(
            [
                it for it in (HotDogTopLevelType.BUN,
                              HotDogTopLevelType.SUASAGE,
                              HotDogTopLevelType.KETCHUP,
                              HotDogTopLevelType.MAYONNAISE,
                              HotDogTopLevelType.MUSTARD,
                              HotDogTopLevelType.PICKLES,
                              HotDogTopLevelType.REDONION)
            ]
        )

    def get_hotdog(self) -> HotDog:
        return self.hotdog

class Director:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder: Builder):
        self.builder = builder

    def make_hotdog(self):
        if not self.builder:
            raise ValueError("Builder didn't set")
        self.builder.sharpness_thick()
        self.builder.add_fastfood()
        self.builder.add_topping()

if __name__ == '__main__':
    director = Director()
    for it in (TraditionalHotDogBuilder, AmericanHotDogBuilder, VillageHotDogBuilder):
        builder = it()
        director.set_builder(builder)
        director.make_hotdog()
        hotdog = builder.get_hotdog()
        print(hotdog)
        print('----------------------------')


dc_Traditional = DiscountCalculatorTraditional(100)
print(dc_Traditional.get_discounted_price())

dc_American = DiscountCalculatorAmerican(100)
print(dc_American.get_discounted_price())

dc_Village = DiscountCalculatorVillage(100)
print(dc_Village.get_discounted_price())