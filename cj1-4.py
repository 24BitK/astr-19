# declares a class describing your favorite animal. 

class FavAnimal:					#Assign features to animal
	def __init__(x,length_arms,length_legs,num_eyes,tail,furry):
		x.length_arms = length_arms
		x.length_legs = length_legs
		x.num_eyes = num_eyes
		x.tail = tail
		x.furry = furry


	def describe(x):
		print(f"Arm length:{x.length_arms} in")
		print(f"Arm length:{x.length_legs} in")
		print(f"Arm length:{x.num_eyes} ")
		print(f"Arm length:{'Yes' if x.tail else 'No'}")
		print(f"Arm length:{'Yes' if x.furry else 'No'}")
	

		#return statement #(if necessary)

		# call the fxn
if __name__ == '__main__':
    my_favorite_animal = FavAnimal(2.5, 3.0, 2, True, False)
my_favorite_animal.describe()

#for x in alpha_dict.keys():
#print(x, alpha_dict[x])

# Write an initialization function that sets the values 
#of the data members when an instance of the class is created. 
#Write a member function of the class to print out and describe 
#the data members representing the physical characteristics of the animal.

# Example fxn:


#—————————————————————————————————
#So in your case you could write something like: