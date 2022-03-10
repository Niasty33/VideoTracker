import math
from random import random

class Point:
    def __init__(self,x = 0,y = 0):
        self.__x = x
        self.__y = y

    def __get__x(self):
        return self.__x

    def __get__y(self):
        return self.__y
    
    def __str__(self):
         return f"( {self.__x} ; {self.__y} )"

def distance(A, B):
    dx = abs(A.__x - B.__x)
    dy = abs(A.__y - B.__y)
    return math.sqrt(dx**2 + dy**2)

def randomPoints(n:int):
    tab = [0]*n
    for k in range(n):
        px = random()
        py= random()
        tab[k] = Point(px,py)
    return tab


if __name__ == "__main__":
    origin = Point()
    p = Point(3,4)
    print(p)
    print(distance(origin, p))
    t = randomPoints(8)
    print(t)

