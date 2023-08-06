import unittest
class Rectangle:
    def __init__(self, width: float ,lenght: float | None = None) -> None:
       self._lenght = lenght
       if width:
           self._width = width
       else:
           self._lenght = lenght

    def get_lenght(self) -> float:
        return 2 * (self._lenght + self._width)

    def get_area(self) -> float:
        return self._width * self._lenght

class TestRectangle(unittest.TestCase):
    def test_method(self):
        self.exp1 = Rectangle(1,1)
        self.exp2 = Rectangle(2,6)

if __name__ == '__main__':
    unittest.main()