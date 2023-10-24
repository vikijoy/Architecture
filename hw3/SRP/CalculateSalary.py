class CalculateSalary:

    baseSalary: int
    valueTime: int

    def __init__(self, base_salary, value_time):
        self.baseSalary = base_salary
        self.valueTime = value_time

    def calculate_salary(self):
        return self.baseSalary * self.valueTime