from material_properties import material_property_library as mp
import pytest


def test_output_class():
    A = {'UO2':{'rho':10.5, 'k':2.5, 'c':332}}
    
    assert isinstance(mp(A), dict)
    
    """The output of the function should be a dictionary"""
    
