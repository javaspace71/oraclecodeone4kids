# Python Program to find the factors of a number

# define a function
def printFactors(x):
   # This function takes a number and prints the factors

   print("************************************")
   print("The factors of",x,"are: ")
   
   for i in range(1, x + 1):
       if x % i == 0:
           print(i, end="  ")
           
           #print(i)

# change this value for a different result.
num = int(input("Enter the number to factorize: "))

printFactors(num)
