# -*- coding: utf-8 -*-
"""
Created on Tue May 23 19:19:26 2017

@author: Ratnadeepb
"""

def grubler_criterion(n, j, d):
    """
    This function returns the DoF of a system according to the Grubler
    Criterion.
    @Input:
        n - Number of links
        j - List:
                len(j) = number of joints
                ith element of j = DoF of the ith joint
        d - 3 dimensional or 2 dimensional system
    @Output:
        degree of freedom of the whole system
    """
    if not isinstance(j, list):
        raise ValueError("Invalid Input")
    if d == 3:
        l = 6
    elif d == 2:
        l = 3
    else:
        raise ValueError("Invalid dimension")
    
    return l * (n - len(j) - 1) + sum(j)

def constraint(n, j, d):
    """
    This function returns the DoF of a system according to the Constraint
    Formulation.
    @Input:
        n - Number of links
        j - List:
                len(j) = number of joints
                ith element of j = DoF of the ith joint
        d - 3 dimensional or 2 dimensional system
    @Output:
        degree of freedom of the whole system
    """
    if not isinstance(j, list):
        raise ValueError("Invalid Input")
    if d == 3:
        l = 6
    elif d == 2:
        l = 3
    else:
        raise ValueError("Invalid dimension")
    
    for i in range(len(j)):
            j[i] = l - j[i]
    
    return l * (n - 1) - sum(j)