# -*- coding: utf-8 -*-
"""
Created on Sun May 14 06:36:11 2017

@author: Ratnadeepb
"""

import numpy as np

# Quaternion Multiplication
def quaternion_product(q1, q2):
    """
    This function returns the product of two quaternions
    
    @Input:
        q1, q2 - The quaternions to be multiplied
    
    @Output:
        q - The product
    """
    
    if not isinstance(q1, np.ndarray):
        try:
            q1 = np.array(q1)
        except:
            raise ValueError("Invalid Input")
    if not isinstance(q2, np.ndarray):
        try:
            q1 = np.array(q1)
        except:
            raise ValueError("Invalid Input")
    
    u0 = q1[0]
    u = q1[1:]
    v0 = q2[0]
    v = q2[1:]
        
    return np.append(np.array(u0 * v0 - u.T.dot(v)), u0 * v + v0 * u - 
                     np.cross(u, v))