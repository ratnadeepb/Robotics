# -*- coding: utf-8 -*-
"""
Created on Tue May 16 08:48:33 2017

@author: Ratnadeepb
"""

import numpy as np
import math

# q0 = np.array([1, 0, 0, 0])

# theta = np.pi/2
# q1 = np.array([np.cos(theta/2), np.sin(theta/2), 0, 0])
q0 = np.array([0.737451860557466, 0.389942198007317, 0.389942198007317, 0.389942198007317])
q1 = np.array([0.861558096653114, 0.293097052237801, 0.293097052237801, 0.293097052237801])
omega = math.acos(np.dot(q0, q1))
steps = 50

if abs(omega) > 2 * np.pi:
    omega %= (2 * np.pi)

if omega > np.pi:
    omega = 2 * np.pi - omega

del_t = 1 / steps
t = del_t

quats = np.zeros((steps, 4))
i = 1

while t <= 1:
    qm = (np.sin((1 - t) * omega / 2) * q0 + np.cos(t * omega) * q1) / np.sin(omega)
    quats[i] = qm
    t += del_t
    i += 1