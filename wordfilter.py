#Give the user some short context about the background of the program
print("This short little program lets the user choose which words to filter out.")

#Have the user create an array of words to filter and seperate each word. These can be swear words, normal words, or any word the user chooses to enter. 
filter_words = input("First, please enter the words (case sensitive) that you'd like to filter out: ").split()

#Have the user input a sentence and seperate each word within the string
user_text = input("Enter some words: ").split()

na = []

#Reprint the inputted phrase but if it's a filtered word, bleep it out
for word in user_text:
	if word in filter_words: #TODO: Fix the bug where a filtered word is not filtured due to being attached to punctuation (i.e. "lorem.")
		print("%*#$", end = " ")
	else:
		print(word, end = " ")







