#from dash import Dash


import numpy as np
import time



start= time.time()
a= np.array([4,2])

print(a)
print(a.shape)
print(a.size)
print(a.ndim)
print(time.time() - start)

name: str= "bob"
age: int= 8
height= 8
print(height)

from typing import Final
VERSION: Final[str]= '1.0.12'
#VERSION= '1.2'  #still mutable but warning
VERSION_INT: Final[float]= 3.14
print(VERSION)
print(VERSION_INT)

#functions
def time() -> None:
    from datetime import datetime
    print(f'This is {datetime.now()} time')

time()
time()

#classes
print()
from typing import  Self
class Car:
    def  __init__(self, colour: str, horsepower:int) ->None :
        self.colour= colour
        self.horsepower= horsepower

    # DUNDER METHODS
    def __str__(self)-> str:
        return f'color={self.colour}, horsepower={self.horsepower}'

    def __add__(self, other: Self)-> str:
        return  f'{self.colour} & {other.colour}'

volvo:Car= Car("yellow", 500)
bmw:Car= Car('orange', 5000)
print("1111")
print(volvo)
print(bmw + volvo)


print("1111")
print()

volvo:Car= Car('red', 200)
print(volvo.colour)
print(volvo.horsepower)
print()
car= Car('red', 5500)
print(car.colour)
print(car.horsepower)
print(car)


print()

class Animal:
    def __init__ (self, name:str, batch: float)-> None:
        self.name=name
        self.batch= batch

    def activity(self, activity: str) -> None:
        print(f"{self.name} is {activity}ing ")
        
dog:Animal= Animal('butcher', 3.14)
print(dog.name)
dog.activity("walk")










