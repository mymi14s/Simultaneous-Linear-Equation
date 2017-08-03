"""
Author: Anthony C. Emmanuel
Title: Simultaneous Equation Solver
Language: Python 3.6
Date: 02-08-2017
License: GPL Latest"""

import numpy as np

def compute(a,b):
	z = np.linalg.solve(a,b)
	return (z)
