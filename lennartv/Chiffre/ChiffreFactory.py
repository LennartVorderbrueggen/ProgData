
from SkytaleChiffre import SkytaleChiffre
from CaesarChiffre import CaesarChiffre
from VigenereChiffre import VigenereChiffre
from ChiffreBase import Chiffre
from enum import Enum

class ChiffreType(Enum):
    SkytaleChiffre = 1
    CaesarChiffre = 2
    VigenereChiffre = 3

class ChiffreFactory():
    @staticmethod
    def CreateChiffre(type: ChiffreType) -> Chiffre:
        match type:
            case ChiffreType.SkytaleChiffre:
                return SkytaleChiffre()
            case ChiffreType.CaesarChiffre:
                return CaesarChiffre()
            case ChiffreType.VigenereChiffre:
                return VigenereChiffre()                  
        