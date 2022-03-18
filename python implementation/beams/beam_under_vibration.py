# Import libraries

from utils import ploting
from .beam import Beam
from sympy import *


class BeamUnderVibration(Beam):
    """
    A class used to represent a beam under vibration
    (A beam that is harnessed on one side and power at the end)

    ...

    Attributes
    ----------

    ... child of beam


    Methods
    -------

    """

    @staticmethod
    def get_parametric_shear_force_function():
        """
        return the parametric shear force function of the beam

        Parameters
        ----------

        Raises
        ------

        """
        force = symbols('p(t)')
        v = force

        return v

    def get_num_shear_force_function(self, force):
        """
        return the shear force function of the beam

        Parameters
        ----------
        force : double (newtons)
            The force acting on the edge of the beam
        Raises
        ------

        """

        num_shear_force_function = self.get_parametric_shear_force_function().subs('p(t)', force)
        return num_shear_force_function

    @staticmethod
    def get_parametric_moment_function():
        """
        return the parametric moment function of the beam

        Parameters
        ----------

        Raises
        ------

        """

        force, length, = symbols('p(t) L_tot')
        x = symbols('x')
        m = force * (length - x)

        return m

    def get_num_moment_function(self, force):
        """
        return the moment function of the beam

        Parameters
        ----------
        force : double (newtons)
            The force acting on the edge of the beam

        Raises
        ------

        """

        length = self.get_total_length()
        num_moment_function = self.get_parametric_moment_function().subs([('p(t)', force), ('L_tot', length)])
        return num_moment_function

    def __init__(self, beam):
        """
        Parameters
        ----------
        beam: Beam
            get beam instance

        """
        super().__init__(beam.name, beam.sections)
