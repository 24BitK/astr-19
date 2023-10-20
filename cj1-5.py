# Write a Python program that writes out a table of the function sin(x) 
#vs. x, where x is tabulated between 0 and 2 with a thousand entries. 
#Follow the basic Python program structure, including a main program function.

import numpy as np

def main():

	#assign parameters
	num_entries = 1000
	start_x = 0
	stop_x = 2*np.pi
	hit = (stop_x - start_x) / (num_entries - 1)

	#print table
	print("{:15} {:15}".format('x', 'sin(x)'))
	print("-" * 30)

	#Iterate values and print
	for i in range(num_entries):
		x = start_x + i * hit
		sin_value = np.sin(x)
		print("{:15} {:15}".format(x, sin_value))

if __name__ == '__main__':
	main()