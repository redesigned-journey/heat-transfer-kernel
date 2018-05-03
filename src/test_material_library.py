import numpy as np
import pytest
from material_properties import material_property_library as mp




def test_fuel_type():
    A = [('UO2',250e-6)]
    B = []
    
    assert(mp(A, B)) ==  {
                'UO2':{'rho':10.5, 'k':2.5, 'layer_thickness': 0.00025, 'c':332}
                         }
                
    """If the user specifies zero cladding, the material library should reflect that."""
        
        
def test_output_class():
    A = [('UO2',250e-6)]
    B = [('Silicon Carbide', 35e-6)]
    
    assert isinstance(mp(A, B), dict)
    
    """The output of the function should be a dictionary"
    
