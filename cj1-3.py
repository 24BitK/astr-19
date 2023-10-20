#defines a function f(x) that returns x**3 + 8. 
#In the main function of the program, call f(x) with x = 9 
#print the result.  
#if statement that executes if the result is larger than 27 prints “YAY!”.

#assign value to x
x = 9
print ("x =",x)
#assigh second variable than apply function
fx = 0
fx = x**3 + 8
#print statement
print("fx = x**3 + 8","," "fx =", fx)
print(fx,"> 27")
if fx > 27:
	print("YAY!")