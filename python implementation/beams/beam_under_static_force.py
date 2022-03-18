# Import libraries

from utils import ploting
from sympy import *
from .beam import Beam


class StaticBeam(Beam):
    """
    A class used to represent a static beam
    (A beam that is harnessed on one side and force at the end)

    ...

    Attributes
    ----------

    ... child of beam


    Methods
    -------

    """

    def __init__(self, beam):
        """
        Parameters
        ----------
        beam: Beam
            get beam instance

        """
        super().__init__(beam.name, beam.sections)

    @staticmethod
    def get_parametric_shear_force_function():
        """
        return the parametric shear force function of the beam

        Parameters
        ----------

        Raises
        ------

        """
        force = symbols('p')
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

        num_shear_force_function = self.get_parametric_shear_force_function().subs('p', force)
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

        force, length = symbols('p L_tot')
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
        num_moment_function = self.get_parametric_moment_function().subs([('p', force), ('L_tot', length)])
        return num_moment_function

    def get_parametric_beam_curvature_function(self,):
        """
        return the beam curvature function

        Parameters
        ----------


        Raises
        ------

        """
        v_total = []
        force, total_length = symbols('p'), symbols('L_tot'),

        for i in range(len(self.sections)):

            elastic_constant, i, section_length = symbols(f'E{i} I{i} L{i}')
            x, c0, c1 = symbols('x c0 c1')

            moment = force * (total_length - x)
            # v'' = -M/EI
            v = -integrate(integrate(moment, x), x) + x * c1 + c0
            v = v/(elastic_constant * i)

            last_v, last_x = (0, 0) if len(v_total) == 0 else (v_total[-1][0], v_total[-1][-1][-1])
            if len(v_total) == 0:
                # start conditions
                v = v.subs(c0, solve(v.subs(x, 0), c0)[0])
                v = v.subs(c1, solve(diff(v, x).subs(x, 0), c1)[0])

            else:
                # edge conditions
                v = v.subs(c0, solve(v.subs(x, last_x) - last_v.subs(x, last_x), c0)[0])
                v = v.subs(c1, solve(diff(v, x).subs(x, last_x) - diff(last_v, x).subs(x, last_x), c1)[0])

            v_total.append((v, (x, last_x, last_x + section_length)))

        return v_total

    def get_num_beam_curvature_function(self, force):
        """
        return the beam curvature function

        Parameters
        ----------
        force : double (newtons)
            The force acting on the edge of the beam

        Raises
        ------

        """

        length = self.get_total_length()
        sections = self.sections
        num_beam_curvature_function = []

        for part_param_function, rng in self.get_parametric_beam_curvature_function():
            num_part_function = part_param_function.subs([('p', force), ('L_tot', length)])
            start_r, end_r = rng[1], rng[2]

            for i in range(len(sections)):
                num_part_function = num_part_function.subs(
                    [(f'E{i}', sections[i].young_modulus),
                     (f'I{i}', sections[i].shape.get_i()),
                     (f'L{i}', sections[i].length)])

                start_r = start_r.subs(f'L{i}', sections[i].length) if type(start_r) != int else 0
                end_r = end_r.subs(f'L{i}', sections[i].length)

            num_beam_curvature_function.append((num_part_function, (rng[0], start_r, end_r)))

        return num_beam_curvature_function

    def get_beam_curvature_in_end(self, force):
        """
        return the beam curvature in the edge of the beam

        Parameters
        ----------
        force : double (newtons)
            The force acting on the edge of the beam

        Raises
        ------

        """

        return self.get_beam_curvature_in_x(force, self.get_total_length())

    def get_beam_curvature_in_x(self, force, x):
        """
        return the beam curvature in specific x

        Parameters
        ----------
        force : double (newtons)
            The force acting on the edge of the beam
        x : double (meter)
            The x to calculate curvature at


        Raises
        ------
        ValueError if x not in the beam range

        """

        if x > self.get_total_length() or x < 0:
            raise ValueError(f'X should be between 0 and beam length ({self.get_total_length()})')
        else:
            return next(function
                        for function, rng in self.get_num_beam_curvature_function(force) if rng[1] < x <= rng[2]
                        ).subs('x', x)

    def show_shear_force_graph(self, force):
        """
        plot a graph of the shear force function of the beam

        Parameters
        ----------
        force : double (newtons)
            The force acting on the edge of the beam

        Raises
        ------

        """

        length = self.get_total_length()
        x = symbols('x')
        num_shear_force_function = self.get_num_shear_force_function(force)

        ploting.customized_plot(x, num_shear_force_function,
                                title="shear force as function of x", label='V(x)',
                                y_axis='V [N]', x_axis='x [m]', length=length)

    def show_moment_graph(self, force):
        """
        plot a graph of the moment function of the beam

        Parameters
        ----------
        force : double (newtons)
            The force acting on the edge of the beam

        Raises
        ------

        """

        length = self.get_total_length()
        num_moment_function = self.get_num_moment_function(force)
        x = symbols('x')

        ploting.customized_plot(x, num_moment_function,
                                title="moment as function of x", label='M(x)', y_axis='M [N*m]',
                                x_axis='x [m]', length=length)

    def show_beam_curvature_graph(self, force):
        """
        plot a graph of the beam curvature function

        Parameters
        ----------
        force : double (newtons)
            The force acting on the edge of the beam

        Raises
        ------

        """

        num_beam_curvature_function = self.get_num_beam_curvature_function(force)

        ploting.customized_plots(num_beam_curvature_function, title="beam curvature as function of x",
                                 label='v(x)', y_axis='v [m]', x_axis='x [m] ')

    def get_str_detailed_description(self):
        """
        return string of detailed description -
        the name of the beam , the sections of the beam , general attributes, the functions

        Parameters
        ----------

        Raises
        ------

        """

        return f'{str(self)}\n\n{self.get_str_general_attributes()}\n\n{self.get_str_parametric_functions()}'

    def get_str_parametric_functions(self):
        """
        return string of the functions - shear force: V(x) , moment: M(x) , beam curvature: v(x)

        Parameters
        ----------

        Raises
        ------

        """

        return f'Parametric functions - \nShear force: V(x) = {self.get_parametric_shear_force_function()}\n' \
               f'Moment: M(x) = {self.get_parametric_moment_function()}\n' \
               f'Beam curvature: v(x) = {self.get_parametric_beam_curvature_function()}'

    def __str__(self):
        """

        return string description of the beam - the name of the beam and the sections of the beam

        Parameters
        ----------

        Raises
        ------

        """

        return f'{self.name} beam \n\nsections -\n{",".join([f"section {i+1}: " + str(self.sections[i]) for i in range(len(self.sections))])}'