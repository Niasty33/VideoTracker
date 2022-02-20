import unittest
import filecmp
import numpy as np
import sys
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)
from src.models import point
from src.models import FileRepo

class Test_FileRepo(unittest.TestCase):

    #TEST N°1
    #On cherche à savoir si les points dans le fichier CSV correspondent aux points rentrés en paramètres
    #Le fichiers lié 'points_attendus' sera notre témoin, 'points' le résultat du programme FileRepo
    def setUp(self, tab=[point.Point(5.3,3.6),point.Point(4.7,9.5),point.Point(15.2,3.3)]):
        self.__tab = tab
        self.__temoin = open('points_attendus.csv','r')
    
    
    def test_fileCSV(self): 
        file = FileRepo.FileRepo(self.__tab)
        file.export2CSV()
        f = open('points.csv','r')
        read_f = np.loadtxt(f, delimiter=";")
        read_temoin = np.loadtxt(self.__temoin, delimiter=";")
        self.assertTrue(read_f is read_temoin)
    #En exécutant ce programme, on constate que le fichier CSV correspond


if __name__ == '__main__':
    tab = [point.Point(5.3,3.6),point.Point(4.7,9.5),point.Point(15.2,3.3)]
    unittest.main(verbosity=2)