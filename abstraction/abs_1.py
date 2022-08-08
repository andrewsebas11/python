from abc import ABC, abstractmethod


class Car(ABC):
    def mileage(self):
        pass

class Hyundai(Car):
    def mileage(self):
        print(f"The average mileage of hyundai car is 16kmpl")

class BMW(Car):
    def mileage(self):
        print(f"The average mileage of BMW car is 14kmpl")

class Audi(Car):
    def mileage(self):
        print(f"The average mileage of Audi car is 14kmpl")\

class Tata(Car):
    def mileage(self):
        print(f"The average of Tata car is 20kmpl")

a = Hyundai()
b = BMW()
c = Audi()
d = Tata()
for z in (a, b, c, d):
    z.mileage()
