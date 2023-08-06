import pytest

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


    def test_pytest(self):
        exp = Rectangle(1,1)
        assert exp.get_lenght() == 2



if __name__ == '__main__':
    pytest.main()
