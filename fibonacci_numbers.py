# Fibonacci numbers   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

# Implment a program that will print a LIST of fibonacci numbers to a specified length.

# Example: fibonacci(10)
# input: number  (desired length of array)
# output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] - the first 10 numbers of the fibonacci sequence

# Hint:
# You may start your array like this:
# list = [0, 1]


# *** your code here ***

def fibonacci(num):
	my_list = [0, 1]
	if num == 1:
	  my_list = [0]
    
	elif num > len(my_list):
		for i in range(num - 2):
			my_list.append(my_list[i] + my_list[i + 1])
  
	  
	print(my_list)
	
	
fibonacci(10)
