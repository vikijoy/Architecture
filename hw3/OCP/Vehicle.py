class Vehicle:
    __max_speed: int
    __vec_type: str

    def __init__(self, max_speed, vec_type):
        self.__max_speed = max_speed
        self.__vec_type = vec_type

    def set_max_speed(self, max_speed):
        self.__max_speed = max_speed

    def get_max_speed(self):
        return self.__max_speed

    def set_vec_type(self, vec_type):
        self.__vec_type = vec_type

    def get_vec_type(self):
        return self.__vec_type

    def calculate_max_speed(self):
        return self.__max_speed