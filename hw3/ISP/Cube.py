from Shape3D import Shape3D


class Cube(Shape3D):
    __side: int

    def __init__(self, side):
        self.__side = side

    def get_side(self):
        return self.__side

    def set_side(self, side):
        self.__side = side

    def perimeter(self):
        return 12 * self.__side

    def value(self):
        return self.__side ** 3