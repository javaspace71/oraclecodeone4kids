# Program to check if a string is palindrome or not

# change this value for a different output
mystr = input('Enter a string to check if it is a palindrome: ')

# make it suitable for caseless comparison
mystr = mystr.lower()

# reverse the string
revstr = reversed(mystr)

# check if the string is equal to its reverse
if list(mystr) == list(revstr):
   print(mystr + " is a palindrome")
else:
   print(mystr + " is not a palindrome")

#able was I ere I saw elba
#malayalam
#racecar
#rotator
