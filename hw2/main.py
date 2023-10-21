import random

from hw2.GemGenerator import GemGenerator
from hw2.GoldGenerator import GoldGenerator
from hw2.SilverGenerator import SilverGenerator
from hw2.CupperGenerator import CupperGenerator

if __name__ == '__main__':
    fabricList = [GemGenerator(), GoldGenerator(), SilverGenerator(), CupperGenerator()]
    for i in range(5):
        rnd = random.choice(fabricList).create_item().open()
