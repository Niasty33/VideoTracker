import unittest
import filecmp
import sys
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)
from src.models import point
from src.models import FileRepo

class Test_FileRepo(unittest.TestCase):
    #TEST N°1
    #On cherche à savoir si les points dans le fichier CSV correspondent aux points rentrés en paramètres
    #Le fichiers lié 'points_attendus' sera notre témoin, 'points' le résultat du programme FileRepo
    tab = [point.Point(5.3,3.6),point.Point(4.7,9.5),point.Point(15.2,3.3)] 
    f = FileRepo.FileRepo(tab)
    f.export2CSV()

