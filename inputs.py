"""
Author: Anthony C. Emmanuel
Title: Simultaneous Equation Solver
Language: Python 3.6
Date: 02-08-2017
License: GPL Latest"""

#input
import numpy as np

my_arrays = []

#input function definition
def inputs():
	while True:
		print("Enter the number of unknowns: ")
		try:
			un = int(input())
			break
		except ValueError:
			print("Please enter a number")


	#initialize the array
	for i in range(un):
		for j in range(un):
			while True:
				try:
					print("Enter ["+str(i)+","+str(j)+"]")
					getval = int(input())
					break
				except ValueError:
					print("Please enter a number")
					
			my_arrays.append(getval)

	#arrays variables to be used
	a=[];b=[];c=[];d=[];e=[];f=[];g=[];h=[]
	n = [a,b,c,d,e,f,g,h]
	# for i in range(un):
	# 	n[i] = []


	#move the column vectors to lists, j=0 as count
	j=0
	for i in range(len(my_arrays)):
		n[j].append(my_arrays[i])
		if((i+1)%un==0):
			j+=1

		

	#intialize the final array
	all_arrays = []
	for i in range(un):
		all_arrays.append(n[i])

	#set the A part of the parameter
	a = np.array(all_arrays)


	#The basis bi
	print("Enter the basis: ")
	b = []
	for i in range(un):
		while True:
			try:
				print("Enter b"+str(i))
				getval = int(input())
				break
			except ValueError:
				print("Please enter a number")
		b.append(getval)

	#Set the B part of the parameter
	b=np.array(b)

	#Hold A and B as a list
	
	return (a,b)
