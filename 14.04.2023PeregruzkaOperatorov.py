#1
# import math
# class Circle:
#     def __init__(self, Radius: int):
#         if not isinstance(Radius, int):
#             raise TypeError("Радиус должен быть целым числом")
#         self.__Radius = Radius
#     def getL(self):
#         return self.__Radius
#     def getC(self):
#         return math.pi*2*self.__Radius
#
#
#     def __eq__(self, other):
#         return self.__Radius == other.__Radius
#
#     def __lt__(self, other):
#         return self.getC() < other.getC()
#
#     def __gt__(self, other):
#         pass
#
#     def __le__(self, other):
#         pass
#
#     def __ge__(self, other):
#         pass
#     def __add__(self, num: int):
#         return Circle(self.__Radius+num)
#     def __iadd__(self, num: int):
#         self.__Radius += num
#     def __sub__(self, num: int):
#         pass
#     def __isub__(self, num: int):
#         pass
#
#
# my_circle = Circle(6)
# my_circle1 = Circle(4)
#
# print(my_circle == my_circle1)
# print(my_circle < my_circle1)
# print(my_circle > my_circle1)
# print(my_circle <= my_circle1)
# print(my_circle >= my_circle1)

#2
# import math
# class Complex:
#     def __init__(self, r, a):
#         self.__re = r*math.cos(a)
#         self.__im = r*math.sin(a)
#
#     def get_re(self):
#         return self.__re
#
#     def set_re(self, v):
#         raise AttributeError
#
#     def del_re(self):
#         raise AttributeError
#
#     re = property(get_re, set_re, del_re, "Действительная часть read-only")
#
#     def get_im(self):
#         return self.__im
#
#     def set_im(self, v):
#         raise AttributeError
#
#     def del_im(self):
#         raise AttributeError
#
#     im = property(get_im, set_im, del_im, "Мнимая часть read-only")
#
#     def __str__(self):
#         if abs(self.__im) > 1.0e-15:
#             if self.__im < 0:
#                 sim = "-"
#             else:
#                 sim = "+"
#             return "("+str(self.__re)+sim+"I*"+str(abs(self.__im)) + ")"
#         else:
#             return "("+str(self.__re)+"+I*0)"
#
#     def toTrig(x, y):
#         if abs(y) > 1.0e-15:
#             return (math.sqrt(x**2+y**2), math.atan(y / x))
#         elif x > 0:
#             return (math.sqrt(x**2+y**2), 0)
#         else:
#             return (math.sqrt(x**2+y**2), math.pi)
#
#     def __add__(self, o):
#         re_sum = self.__re+o.__re
#         im_sum = self.__im+o.__im
#         (r_sum, a_sum) = Complex.toTrig(re_sum, im_sum)
#         return Complex(r_sum, a_sum)
#
#     def __sub__(self, o):
#         re_sub = self.__re-o.__re
#         im_sub = self.__im-o.__im
#         (r_sub, a_sub) = Complex.toTrig(re_sub, im_sub)
#         return Complex(r_sub, a_sub)
#
#     def __mul__(self, o):
#         re_pro = self.__re*o.__re-self.__im*o.__im
#         im_pro = self.__im*o.__re+self.__re*o.__im
#         (r_pro, a_pro) = Complex.toTrig(re_pro, im_pro)
#         return Complex(r_pro, a_pro)
#
#     def __truediv__(self, o):
#         a = self.__re
#         b = self.__im
#         c = o.__re
#         d = o.__im
#         zz = c**2+d**2
#         aa = (a*c+b*d)/zz
#         bb = (b*c-a*d)/zz
#         (r_div, a_div) = Complex.toTrig(aa, bb)
#         return Complex(r_div, a_div)
#
#     def cabs(self):
#         return math.sqrt(self.__re**2+self.__im**2)
#
# с1 = Complex(1, 3.14/2)
# с2 = Complex(1, 0)
# с3 = с1+с2
# с4 = с1/с2
# с5 = с1*с2
# с6 = с1-с2
# print(с4, с6, с5)

#3
import math
# class Airplane:
#     def __init__(self, passengers: int):
#          if not isinstance(passengers, int):
#              raise TypeError("Пассажир должен быть целым числом")
#          self.__passengers = passengers
#      def getP(self):
#          return self.__passengers
#
#     def __eq__(self, other):
#          return self.__passengers == other.__passengers
#
#     def __add__(self, num: int):
#          return Airplane(self.__passengers+num)
#
#      def __iadd__(self, num: int):
#          self.__passengers+=num
#
#      def __sub__(self, num: int):
#          pass
#
#      def __isub__(self, num: int):
#          pass
#
#     def __gt__(self, other):
#          pass
#
#     def __lt__(self, other):
#          return self.getP() < other.getP()
#
#     def __le__(self, other):
#          pass
#
#      def __ge__(self, other):
#          pass
#
# my_air = Airplane(50)
# my_air1 = Airplane(60)
#
# print(my_air == my_air1)
# print(my_air < my_air1)
# print(my_air > my_air1)
# print(my_air <= my_air1)
# print(my_air >= my_air1)

#4
import math
class Flat:
    def __init__(self, price, square: int):
          self.__price = price
          self.__square = square

    def getP(self):
          return self.__price
    def getS(self):
          return self.__square

    def __eq__(self, other):
          return self.__square == other.__square

    def __ne__(self, other):
          return self.__square != other.__square

    def __gt__(self, other):
          pass

    def __lt__(self, other):
          return self.getP() < other.getP()

    def __le__(self, other):
          pass

    def __ge__(self, other):
          pass

my_flat = Flat(3000000,33)
my_flat1 = Flat(4500000,48)

print(my_flat == my_flat1)
print(my_flat != my_flat1)
print(my_flat < my_flat1)
print(my_flat > my_flat1)
print(my_flat <= my_flat1)
print(my_flat >= my_flat1)