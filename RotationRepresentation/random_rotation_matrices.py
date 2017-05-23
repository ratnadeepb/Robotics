# -*- coding: utf-8 -*-
"""
Created on Sun May 14 08:47:59 2017

@author: Ratnadeepb
"""

import numpy as np
from numpy import linalg as la
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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
    return orthogonalization(np.random.rand(9).reshape(3,3))

def plot_rotation(u, v):
    """
    This function will plot u and v vectors in 3D
    """
    fig = plt.figure()
    ax = Axes3D(fig)
    xx, yx, zx = [1, 0], [0, 0], [0, 0]
    xy, yy, zy = [0, 0], [0, 1], [0, 0]
    xz, yz, zz = [0, 0], [0, 0], [0, 1]
    x0, y0, z0 = [0, u[0]], [0, u[1]], [0, u[2]]
    x1, y1, z1 = [0, v[0]], [0, v[1]], [0, v[2]]
    ax.plot(xx, yx, zx, 'r')
    ax.text(1, 0, 0, 'x')
    ax.plot(xy, yy, zy, 'g')
    ax.text(0, 1, 0, 'y')
    ax.plot(xz, yz, zz, 'b')
    ax.text(0, 0, 1, 'z')
    ax.plot(x0, y0, z0, 'k', linestyle=':')
    ax.text(u[0], u[1], u[2], '({:.3f},{:.3f},{:.3f})'.format(u[0], u[1], u[2]))
    ax.plot(x1, y1, z1, 'k', linestyle='--')
    ax.text(v[0], v[1], v[2], '({:.3f},{:.3f},{:.3f})'.format(v[0], v[1], v[2]))
    plt.show()

def rotate():
    """
    This function will choose a u vector in random
    Generate the R matrix
    Rotate u by R to v
    Plot v
    Return v
    """
    u = np.random.rand(3)
    R = random_rotation()
    v = R @ u
    plot_rotation(u, v)
    return v