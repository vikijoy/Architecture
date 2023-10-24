from Engine import Engine


class Car:
    __engine: Engine

    def __init__(self, engine: Engine):
        self.__engine = engine

    def get_engine(self):
        return self.__engine

    def set_engine(self, engine: Engine):
        self.__engine = engine

    def start(self):
        self.__engine.start()