import numpy as np
import pytest
from random import randint
import numpy.linalg as linalg
import sys
sys.path.insert(0, '../src')
from matrix_solver import solve_matrix as sm


def test_output_array():

    A = np.ones((1, 1))
    b = np.ones(1)
    assert isinstance(sm(A, b), np.ndarray), \
        "the output temperature should be an array."


def test_output_1():

    A = np.ones((1, 1))
    b = np.ones(1)

    assert sm(A, b) == 1


def test_output_2():

    A = np.array([[1, 1], [15, 50]])
    b = np.array([[6], [20]])

    assert sm(A, b).shape == b.shape


def test_output_3():

    A = np.array([[5, -6, -7], [6, -4, 10], [2, 4, -3]])
    b = np.array([[7], [-34], [29]])

    assert np.allclose(sm(A, b), np.array([[2], [4], [-3]]))


def test_output_4():

    N = randint(1, 20)
    A = np.random.rand(N, N)
    x = np.ones((N, 1))

    b = np.dot(A, x)

    assert np.allclose(sm(A, b), x)


def test_singular():

    N = randint(1, 20)
    A = np.arange(N**2).reshape((N, N))
    b = np.ones((N, 1))

    assert sm(A, b) == False
