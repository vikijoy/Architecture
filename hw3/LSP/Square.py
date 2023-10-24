from QuadRangle import QuadRangle


class Square(QuadRangle):
    __length: int

    def __init__(self, length):
        self.__length = length

    def area(self):
        return self.__length ** 2

    def get_length(self):
        return self.__length

    def set_length(self, length):
        self.__length = length