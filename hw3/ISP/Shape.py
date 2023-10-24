import zope.interface


class Shape(zope.interface.Interface):
    def perimeter(self):
        pass