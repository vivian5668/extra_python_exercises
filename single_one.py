# Given an array of integers, every element appears twice except for one.
# Implement a program that will print that single one.

# Example: [1,1,2,2,3,3,4,5,5,6,6,7,7] - 4 would be the odd man out

# Note:
# Your algorithm should have a linear runtime complexity.


# *** your code here ***


dd = {}

def find_odd(my_list):
	for i in range(len(my_list)):
		dd[my_list[i]] = my_list.count(my_list[i])
	print(dd)
	for key in dd:
	  if dd[key] == 1:
	    print(key)
	
find_odd([1,1,2,2,3,3,4])
