# Reverse Strings in a Sentence

# Given a string, implement a program that will reverse the order of the characters
# in each word within a sentence while still preserving whitespaces and initial word order.

# Example:
# Input: "Let's do a coding challenge"
# Output: "s'teL od a gniedoc egnellahc"


# *** your code here ***

def reverse(sentence):
	new_sentence = sentence.split(' ')
	result = []
	for word in new_sentence:
	  word = word[::-1]
	 # print(word)
	 # result += [word]
	  result.append(word)
	result = ' '.join(result)
	print(result)

reverse("Let's do a coding challenge")
