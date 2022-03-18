
import math


class Shape:
    """
    A class used to represent a shape of section

    ...

    Attributes
    ----------
    Methods
    -------

    """

    def __init__(self):
        """
        Parameters
        ----------

        """


class Rectangle(Shape):
    """
        A class used to represent rectangle shape

        ...

        Attributes
        ----------
        height : double (meters)
            the height

        width : double (meters)
            the width

        Methods
        -------

    """

    def __init__(self, height, width):
        super().__init__()
        self.height = height
        self.width = width

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return 2 * (self.height + self.width)

    def get_i(self):
        return self.width * self.height ** 3 / 12

    def __str__(self):
        """

        return string description of the circle - radius , area , perimeter , I

        Parameters
        ----------

        Raises
        ------

        """

        return f'Rectangle - Height: {self.height} meter, Width: {self.width} meter,' \
               f' Area: {self.get_area()}, Perimeter:{self.get_perimeter()}, I:{self.get_i()}'


class Square(Rectangle):
    """
        A class used to represent square shape

        ...

        Attributes
        ----------
        length : double (meters)
            the length

        Methods
        -------

    """

    def __init__(self, length):
        super().__init__(length, length)


class Circle(Shape):
    """
            A class used to represent circle shape

            ...

            Attributes
            ----------
            radius : double (meters)
                the radius

            Methods
            -------

            """
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def get_i(self):
        return math.pi * self.radius ** 4 / 4

    def __str__(self):
        """

        return string description of the circle - radius , area , perimeter , I

        Parameters
        ----------

        Raises
        ------

        """

        return f'Circle - Radius: {self.radius} meter,' \
               f' Area: {self.get_area()}, Perimeter:{self.get_perimeter()}, I:{self.get_i()}'
