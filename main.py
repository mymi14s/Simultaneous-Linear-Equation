"""
Author: Anthony C. Emmanuel
Title: Simultaneous Equation Solver
Version: 1
Language: Python 3.6
Date: 02-08-2017
License: GPL Latest"""

import result as rs
import compute as cp
import inputs as ip
import numpy as np
print("Simultaneous Equation Solver\nAuthor:Anthony C. Emmanuel\nDate:02-08-2017\n")

while True:
	getva=ip.inputs()
	a,b = getva
	z = cp.compute(a,b)
	print("\nThe result: \n")
	rs.result(z)
	print("\n")