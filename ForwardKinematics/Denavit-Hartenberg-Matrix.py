# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 10:38:17 2017

@author: Ratnadeepb
"""

import numpy as np

def Denavit_Hartenberg_Matrix(r, alpha, d, theta):
    """
    This method returns the transformation matrix from the Denavit
    Hartenberg parmaters
    
    @Inputs:
        r       -   length of common normal
        alpha   -   angle about common normal from previous z-axis to next
                    z-axis
        theta   -   angle about previous z from previous x-axis to next 
                    x-axis
        d       -   offset along previous z to common normal
    @Output:
        A 4 x 4 transformation matrix from previous coordinate system to next
        coordinate system.
    """
    
    if theta < 0:
        theta = 2 * np.pi - theta
    if alpha < 0:
        alpha = 2 * np.pi - alpha
    
    theta = theta % (2 * np.pi)
    alpha = alpha % (2 * np.pi)
    
    s_t = np.sin(theta)
    s_a = np.sin(alpha)
    c_t = np.cos(theta)
    c_a = np.cos(alpha)
    
    T = np.array([[c_t, -(s_t * c_a), (s_t * s_a), r * c_t],
        [s_t, (c_t * c_a), -(c_t * s_a), (r * s_t)],
        [0, s_a, c_a, d],
        [0, 0, 0, 1]])
    
    return T