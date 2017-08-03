"""
Author: Anthony C. Emmanuel
Title: Simultaneous Equation Solver
Language: Python 3.6
Date: 02-08-2017
License: GPL Latest"""

def result(z):
	length = len(z)

	ltz = ['X','Y','Z','A','B','C','D']

	for i,j in enumerate(z):
		print(str(ltz[i])+" = "+str(j))