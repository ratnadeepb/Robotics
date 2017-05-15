# -*- coding: utf-8 -*-
"""
Created on Thu May 11 12:08:51 2017

@author: Ratnadeepb
"""

# Conversion between Angle-Axis and Rotation Matrix Representations

import numpy as np
from numpy import linalg as la
import math

# Conversion from Rotation Matrix to Angle-Axis Representations
def matrix2vector(R):
    """
    This function returns the axis of rotation and the angle of the axis.
    @Input:
        R - The rotation matrix
    @Output:
        v - The axis of rotation
        theta - The angle of rotation. This angle is expressed in degrees
    """

    # Verifying input
    
    # Check that input is a matrix
    if not isinstance(R, np.ndarray):
        try:
            R = np.array(R, dtype=np.float64)
        except:
            raise ValueError("Invalid input")
    # Assert R is 2-dimensinal array
    assert len(R.shape) == 2, "Two dimensional inputs only"
    # Check R is square
    assert R.shape[0] == R.shape[1], "Square matrix inputs only"
    
    rotation_property = True

    elems = R.T.dot(R)
    diagonals = elems.diagonal()

    # Check diagonals of R.T.dot(R) are all 1
    for i in diagonals:
        if i < 1 - 0.1 or i > 1 + 0.1:
            rotation_property = False
    if not rotation_property:
        raise ValueError("Invalid Input")
    
    # Check non-diagonals of R.T.dot(R) are all 0
    non_diags = [i for i in elems if i not in diagonals]
    for i in non_diags:
        if i > 1e-10:
            rotation_property = False
    if not rotation_property:
        raise ValueError("Invalid Input")
    
    # Check det(R) = 1
    d_R = la.det(R)
    if d_R < 1 - 0.1 or d_R > 1 + 0.1:
        rotation_property = False
    if not rotation_property:
        raise ValueError("Invalid Input")
    
    # Start of Calculations
        theta = np.rad2deg(math.acos((R.diagonal().sum() - 1) / 2))
    
    if theta == 0:
        v = np.array([np.NaN, np.NaN, np.NaN])
    else:
        eig = la.eig(R)
        eig_vals, eig_vectors = eig[0], eig[1]
        v = np.array(eig_vectors[0].shape)
        
        for i, e in enumerate(eig_vals):
            e = np.real(e)
            if e > 1 - 0.1 and e < 1 + 0.1:
                v = np.real(eig_vectors[:,i])
    
    theta = np.rad2deg(math.acos((R.diagonal().sum() - 1) / 2))
    
    return [v, theta]

def vector2matrix(v, theta):
    """
    This function returns the axis of rotation and the angle of the axis.
    @Input:
        v - The axis of rotation
        theta - The angle of rotation. This angle is expected in radians
    @Output:
        R - The rotation matrix
    """
    if not isinstance(v, np.ndarray):
        try:
            v = np.array(v)
        except:
            raise ValueError("Invalid input")
    
    s = math.sin(theta)
    c = 1 - math.cos(theta)
    
    norm_v = la.norm(v)
    v_cap = v
    
    if norm_v < 1 - 0.1 and norm_v > 1 + 0.1:
        v_cap = v / norm_v
    
    J = np.array([[0, -v_cap[2], v_cap[1]], 
         [v_cap[2], 0, -v_cap[0]], 
         [-v_cap[1], v_cap[0], 0]])
    
    R = np.eye(3) + s * J + c * J.dot(J)
    
    return R

if __name__ == "__main__":
    R = np.array([[ 0.872, -0.48 ,  0.096],
       [ 0.48 ,  0.8  , -0.36 ],
       [ 0.096,  0.36 ,  0.928]])
    R = np.array(R)
    v, theta = matrix2vector(R)
    print("Matrix to Vector")
    print("The axis of rotation is: ", v)
    print("The angle of rotation is ", theta, " degrees")
    print("=====================================================")
    print("Vector to Matrix")
    R_r = vector2matrix(v, np.deg2rad(theta))
    print(R)
