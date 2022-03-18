# Import libraries
from beams.beam import Beam
from beams.beam_under_static_force import StaticBeam
from beams.beam_under_vibration import BeamUnderVibration
from structural_classes.cross_section import CrossSection
from structural_classes.shape import Rectangle, Circle


force_on_edge = 7.5  # force in newtons

# physical beam creation

sections = [
    CrossSection(length=0.1, shape=Rectangle(height=0.01, width=0.01), young_modulus=2e9),
    CrossSection(length=0.05, shape=Circle(radius=0.01), young_modulus=2e9)
]
beam = Beam(name="lol", sections=sections)

# End

print(beam.get_str_detailed_description())

# static force beam
beam_static = StaticBeam(beam)
print(beam_static.get_str_parametric_functions())
print(f'beam_curvature_in_end - {beam_static.get_beam_curvature_in_end(force=force_on_edge)}')
beam_static.show_moment_graph(force=force_on_edge)
beam_static.show_beam_curvature_graph(force=force_on_edge)

# beam under vibration
beam_vibration = BeamUnderVibration(beam)


