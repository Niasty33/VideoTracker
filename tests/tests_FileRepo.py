import unittest
import filecmp
import numpy as np
import sys
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)
from src.models import point
from src.models import FileRepo

class Test_FileRepo(unittest.TestCase):

    def setUp(self):
        self.__tab = [point.Point(5.3,3.6),point.Point(4.7,9.5),point.Point(15.2,3.3)]
        self.__temoin1 = open('tests/fichier_vide.csv','r')
        self.__temoin2 = open('tests/points_attendus.csv','r')
    
    #TEST N°1
    #On cherche à savoir si le fichier est vide
    def test_estVide(self):
        file = FileRepo.FileRepo()
        file.export2CSV()
        f = open('tests/points.csv','r')
        read_f = np.loadtxt(f, delimiter = ";") #transforme le fichier csv en tableau python
        read_temoin = np.loadtxt(self.__temoin1, delimiter = ";")
        self.assertTrue(read_f.all() == read_temoin.all()) #prend toutes les valeurs des tableaux et les compare deux à deux
    # En executant ce programme, on constate que le fichier CSV correspond
          
    #TEST N°2
    #On cherche à savoir si les points dans le fichier CSV correspondent aux points rentrés en paramètres
    #Le fichiers lié 'points_attendus' sera notre témoin, 'points' le résultat du programme FileRepo
    def test_fileCSV(self): 
        file = FileRepo.FileRepo(self.__tab)
        file.export2CSV()
        f = open('tests/points.csv','r')
        read_f = np.loadtxt(f, delimiter = ";") #transforme le fichier csv en tableau python
        read_temoin = np.loadtxt(self.__temoin2, delimiter = ";")
        self.assertTrue(read_f.all() == read_temoin.all()) #prend toutes les valeurs des tableaux et les compare deux à deux
    #En exécutant ce programme, on constate que le fichier CSV correspond

if __name__ == '__main__':
    #tab = [point.Point(5.3,3.6),point.Point(4.7,9.5),point.Point(15.2,3.3)]
    unittest.main(verbosity=2)
