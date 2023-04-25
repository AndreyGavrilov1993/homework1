# #1
# class Device():
#     def __init__(self, name):
#         self._name=name
#     def get_name(self):
#         return self._name
# class Grinder(Device):
#     def __init__(self, name, model, grind):
#         super().__init__(name)
#         self.model = model
#         self.grind = grind
# class CoffeeMachine(Device):
#     def heating(self):
#         print(self._name,"heating")
# class Blender(Grinder):
#     def speed(self):
#         print(self._name,"speed")
#
# class MeatGrinder(Grinder):
#     def __init__(self,name, model, grind, nozzles):
#         super().__init__(name, model, grind)
#         self.nozzles=nozzles
#     def revers(self):
#         print(self._name,"revers")
#
# if __name__=="__main__":
#     grinder1 = CoffeeMachine('Bosh')
#     print(grinder1.get_name())
#     grinder2 = Blender('Vitek','VT-1459 G','Blade')
#     grinder2.speed()

#2
# class Ship:
#     def __init__(self, name):
#         self._name=name
#     def get_name(self):
#         return self._name
# class Frigate(Ship):
#     def warship(self):
#         print(self._name,"warship")
# class Destroyer(Frigate):
#     def heavier(self):
#         print(self._name,"heavier")
#     def great_firepower(self):
#         print(self._name,"great firepower")
#     def faster(self):
#         print(self._name,"faster")
# class Cruiser(Ship):
#     def big(self):
#         print(self._name,"big")
#     def passenger(self):
#         print(self._name,"passenger")
#
# if __name__=="__main__":
#     ship1 = Frigate('Light')
#     print(ship1.get_name())
#     ship2 = Destroyer('Flame')
#     print(ship2.get_name())
#     ship3 = Cruiser('Adventure')
#     print(ship3.get_name())

#3
class Money():
    def __init__(self, name, unit, num, denum):
        self.name=name
        self.unit=unit
        self.num=num
        self.denum=denum
    def get_name(self):
        return self.name
    def summ(self,money2):
        num1=self.num+self.denum*self.unit
        num2=money2.num+money2.denum*money2.unit
        result_num=num1*money2.denum+num2*self.denum
        result_denum=self.denum*money2.denum
        result_unit=result_num//result_denum
        result_num%=result_denum
        return (f'{result_unit},{result_num}/{result_denum}')

    def show(self):
        print(f'{self.unit+self.num/self.denum}')

    def __iadd__(self, other):
            return self.show()+other.show()

money1 = Money(5,2,3,5)
money2 = Money(5,1,8,3)
money3 = Money(6,5,3,7)
money1.show()
money2.show()

