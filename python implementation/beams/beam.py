
class Beam(object):
    """
    A class used to represent a beam

    ...

    Attributes
    ----------

    name : str
        the name of the beam
    sections : list
        list of cross sections in the beam


    Methods
    -------

    """

    def __init__(self, name, sections):
        """
        Parameters
        ----------
        name : str
            The name of the beam
        sections : list
            list of cross sections in the beam

        """

        self.name = name
        self.sections = sections

    def get_str_detailed_description(self):
        """
        return string of detailed description -
        the name of the beam , the sections of the beam , general attributes.

        Parameters
        ----------

        Raises
        ------

        """

        return f'{str(self)}\n\n{self.get_str_general_attributes()}\n'

    def get_str_general_attributes(self):
        """
        return string of general attributes - the name of the beam and the sections of the beam

        Parameters
        ----------

        Raises
        ------

        """

        return f'General attributes - \nLength of the beam : {self.get_total_length()},' \
               f' Volume of he beam: {self.get_total_volume()}'

    def get_total_length(self):
        """
        return the total length of the beam
        the sum of the sections lengths

        Parameters
        ----------

        Raises
        ------

        """

        return sum([s.length for s in self.sections])

    def get_total_volume(self):
        """
        return the total volume of the beam
        the sum of the sections volumes

        Parameters
        ----------

        Raises
        ------

        """

        return sum([s.get_volume() for s in self.sections])

    def __str__(self):
        """

        return string description of the beam - the name of the beam and the sections of the beam

        Parameters
        ----------

        Raises
        ------

        """

        return f'{self.name} beam \n\nsections -\n{",".join([f"section {i+1}: " + str(self.sections[i]) for i in range(len(self.sections))])}'