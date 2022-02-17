from random import random
from VideoTracker/scr//models import point
def randomPoints(n:int):
    tab = [0]*n
    for k in range(n):
        px = random()
        py= random()
        tab[k] = Point(px,py)
    return tab

if __name__ == "__main__":
    t = randomPoints(8)
    print(t)