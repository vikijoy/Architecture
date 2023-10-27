from datetime import datetime, timedelta
from random import uniform, choice, randint


class Ticket:
    __price: str
    __seat: str
    __serial_number: int
    __date: datetime.date
    __base_serial_number = 1
    __is_valid = True

    def __init__(self):
        current_date = datetime.now().date()
        start_date = current_date - timedelta(days=30)
        end_date = current_date + timedelta(days=30)
        self.is_valid = True
        self.price = f'{uniform(30, 1000):02.2f}'
        self.__date = choice([start_date + timedelta(days=x) for x in range((end_date - start_date).days + 1)])
        self.seat = choice(['A', 'B', 'C', 'D']) + str(randint(1, 100))

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.__serial_number = cls.__base_serial_number
        cls.__base_serial_number += 1
        return instance

    def __repr__(self):
        return (f"Ticket(price: {self.price}\n"
                f"    seat: {self.seat}\n"
                f"    serial_number: {self.__serial_number}\n"
                f"    date: {self.__date}\n"
                f"    is_valid: {self.is_valid}\n")

    def set_is_valid(self, validation: bool):
        self.is_valid = validation

    def get_is_valid(self):
        return self.is_valid

    def getDate(self):
        return self.__date

    def getSerialNumber(self):
        return self.__serial_number