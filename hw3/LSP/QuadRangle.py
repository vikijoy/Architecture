from abc import ABC, abstractmethod


class QuadRangle(ABC):
    @abstractmethod
    def area(self):
        print('parent method')