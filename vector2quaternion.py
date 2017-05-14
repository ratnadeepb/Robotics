# -*- coding: utf-8 -*-
"""
Created on Sun May 14 19:00:46 2017

@author: Ratnadeepb
"""

# Axis-Angle to Quaternion

import numpy as np
from numpy import linalg as la
import math

def vector2quaternion(v, theta):
    """
    This function converts vectors and angles to quaternions
    @Input:
        v - Axis of rotation; norm(v) = 1
        theta - Angle of rotation, in radians
    @Output:
        Quaternion computed from v and theta
    """
    if not isinstance(v, np.ndarray):
        try:
            v = np.array(v)
        except:
            raise ValueError("Invalid Input")
    
    v_n = la.norm(v)
    if v_n < 1 + 0.1 or v_n > 1 + 0.1:
        v = v / v_n
    
    return np.append(np.array([math.cos(theta / 2)]), 
                     np.array([math.sin(theta / 2) * v]))

def quaternion2vector(q):
    """
    This function converts quaternions to vectors and angles
    @Input:
        q - quaternion
    @Output:
        v - Axis of rotation
        theta - Angle of rotation
    """
    if not isinstance(q, np.ndarray):
        try:
            q = np.array(q)
        except:
            raise ValueError("Invalid Input")
    
    theta = 2 * math.acos(q[0])
    v = q[1:] / math.sin(theta / 2)
    return [v, theta]