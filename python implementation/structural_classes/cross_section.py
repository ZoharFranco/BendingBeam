
class CrossSection:
    """
    A class used to represent a cross section

    ...

    Attributes
    ----------

    young_modulus : double (Pa | N/m^2)
            the young modulus of the section

    length : double (meter)
        The name of the beam

    shape : Shape
        shape of the cross section



    Methods
    -------

    """

    def __init__(self, length, shape, young_modulus):
        """
        Parameters
        ----------
        young_modulus : double (Pa | N/m^2)
            the young modulus of the section

        length : double (meter)
            The name of the beam

        shape : Shape
            shape of the cross section


        """

        self.length = length
        self.shape = shape
        self.young_modulus = young_modulus

    def get_area(self):
        return self.shape.get_area()

    def get_perimeter(self):
        return self.shape.get_perimeter()

    def get_volume(self):
        return self.length * self.get_area()

    def get_(self, sound=None):
        """

        Parameters
        ----------


        Raises
        ------

        """
    def __str__(self):
        """

        return string description of the section - the young modulus, the length of the section, the shape + shape's attributes

        Parameters
        ----------

        Raises
        ------

        """

        return f'Young modulus: {self.young_modulus} Gpa, Length: {self.length} meter, Shape: {self.shape}'