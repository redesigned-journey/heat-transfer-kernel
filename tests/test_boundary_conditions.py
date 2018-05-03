import pytest
import numpy as np
import sys 
sys.path.insert(0, '../src')
from boundary_conditions import boundary_conditions

def test_bc_type():
    
    part_outer_rad = 10
    boundary_temp = 1

    assert type(boundary_conditions(part_outer_rad, boundary_temp))==list


def test_bc():

    part_outer_rad = 10
    boundary_temp = 1

    assert pytest.approx(boundary_conditions(part_outer_rad, boundary_temp),[part_outer_rad, boundary_temp])
