from Car import Car
from DiselEngine import DiselEngine
from PetrolEngine import PetrolEngine


if __name__ == '__main__':
    eng = PetrolEngine()
    car = Car(eng)
    car.start()
    eng = DiselEngine()
    car = Car(eng)
    car.start()