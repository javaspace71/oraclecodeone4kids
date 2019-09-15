# Program to sort the words in a sentence alphabetically

mystr = input("Enter a sentence to be sorted alphabetically: ")

# breakdown the string into a list of words
words = mystr.split()

# sort the list
words.sort()

# display the sorted words

print("The sorted words are:")
for word in words:
   print(word)
