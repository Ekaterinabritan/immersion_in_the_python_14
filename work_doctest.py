

class Rectangle:
    """
    Check the width and length of the rectangle.
    We count the area and perimeter
    Launching via the console

    >>> from work_doctest import *
    >>> exp = Rectangle(3,4)
    >>> exp.get_lenght()
         14
    >>> exp.get_area()
         12

    Testing number two
    >>> exp = Rectangle(2,5)
    >>> exp.get_lenght()
    14
    >>> exp.get_area()
    10
     """
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


if __name__ == '__main__':
    import doctest
    doctest.testmod()