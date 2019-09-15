#simple assignments of int, float, string
myint1 = 10
print(myint1)
myint2 = int(42)
print(myint2)

myfloat1 = 7.0
print(myfloat1)
myfloat2 = float(8)
print(myfloat2)

mystring1 = 'hello'
print(mystring1)
mystring2 = "student"
print(mystring2)
print(mystring1 + " " + mystring2)

#Including quotes in the printing
mystring3 = "I don't know if I can include apostrophes or 'quotes'"
mystring4 = 'Can\'t I print \'single\' or "double" quotes by escaping the single quote?'
mystring5 = "I can also print \"double quotes\" by escaping \" with a \\ !"
print(mystring3)
print(mystring4)
print(mystring5)

#multiple assignments in one line
a, b, c, d, e = 3, 4, 5.5, "hi", True
print(a,b,c, d, e)

# This will not work!
one = 1
two = 2
three = "hello"
#print(one + two + hello)

#This will work
print(str(one) + str(two) + three)

#String fun
mystrvar1 = "student"
mylongstrvar1 = "I really like python strings and would like to know how they are stored in memory." \
                "Will it still keep two long sentences in the same location?"

lenstr1 = len(mystrvar1)
lenstr2 = len(mylongstrvar1)
print("length of lenstr1", lenstr1)
print("length of lenstr2", lenstr2)

i1 = mystrvar1.index("d")
i2 = mylongstrvar1.index("y")
print("position or index of d", i1)
print("position or index of y", i2)

count_t = mystrvar1.count("t")
count_y = mylongstrvar1.count("y")
print("count of t", count_t)
print("count of y", count_y)

astring = "Hello Student, how are you?"
print(astring.upper())
print(astring.lower())

words = astring.split(" ")
print(words)


'''

#Where do the variables live in computer memory?
#strings are immutable
mystrvar1 = "student"
mystrvar2 = "student"
mystrvar12 = "stu" + "dent"
mystrvar3 = "hello"
#mystrvar1 = "SKP"
print ( "mystrvar1: ", id(mystrvar1) )
print ( "mystrvar2: ", id(mystrvar2) )
print ( "mystrvar12:", id(mystrvar12) )
print ( "mystrvar3: ", id(mystrvar3) )
'''


#print ( id(mystrvar1) )
mylongstrvar1 = "I really like python strings and would like to know how they are stored in memory." \
                "Will it still keep two long sentences in the same location?"
mylongstrvar2 = "I really like python strings and would like to know how they are stored in memory." \
                "Will it still keep two long sentences in the same location?"
mylongstrvar3 = """I really like python strings and would like to know how they are stored in memory.
                 Will it still keep two long sentences in the same location?"""
mylongstrvar4 = """I really like python strings and would like to know how they are stored in memory.
                 Will it still keep two long sentences in the same location?"""

'''
print ( "mylongstrvar1: ", id(mylongstrvar1) )
print ( "mylongstrvar2: ", id(mylongstrvar2) )
print ( "mylongstrvar3: ", id(mylongstrvar3) )
print ( "mylongstrvar4: ", id(mylongstrvar4) )

myintvar1 = 5
myintvar2 = 5
print( "myintvar1: ", id(myintvar1) )
print( "myintvar2: ", id(myintvar2) )
'''


