# -*- coding: utf-8 -*-
"""
Created on Sun May 14 08:47:59 2017

@author: Ratnadeepb
"""

import numpy as np
from numpy import linalg as la

# Generating Random Rotation Matrices
def projection(u, v):
    """
    This function creates the projection of v on u
    """
    return v.dot(u) / (la.norm(u) ** 2)

def orthogonalization(R):
    """
    This function transforms the matrix R to an orthonormal matrix with 
    determinant R.
    That is a rotation matrix.
    """
    u0 = R[:, 0]
    u1 = R[:, 1] - projection(u0, R[:, 1]) * u0
    u2 = R[:, 2] - projection(u0, R[:, 2]) * u0 - projection(u1, R[:, 2]) * u1
    
    R[:, 0] = u0 / la.norm(u0)
    R[:, 1] = u1 / la.norm(u1)
    R[:, 2] = u2 / la.norm(u2)
    
    if la.det(R) == -1:
        R = R / (- 1)
    
    return R

def random_rotation():
    """
    This function creates a random rotation matrix
    """
    return orthogonalization(1 * np.random.randn(9).reshape(3,3))