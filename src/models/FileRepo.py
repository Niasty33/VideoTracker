from point import *


class FileRepo(object):
    def __init__(self,tab=[]):
        self.tab = tab

    def export2CSV(self):
        file = open('tests/points.csv','w')
        for k in range(len(self.tab)):
            line = f"{self.tab[k].x} ; {self.tab[k].y}\n"
            file.write(line)
        file.close()


if __name__ == "__main__":
    t = randomPoints(8)
    f = FileRepo(t)
    f.export2CSV()
