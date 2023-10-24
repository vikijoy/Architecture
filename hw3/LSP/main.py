from QuadRangle import QuadRangle
from Rectangle import Rectangle
from Square import Square


def print_area(quad: QuadRangle):
    print(quad.area())


if __name__ == '__main__':
    rect = Rectangle(3, 4)
    print_area(rect)
    square = Square(4)
    print_area(square)