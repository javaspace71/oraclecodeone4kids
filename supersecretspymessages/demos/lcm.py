# Python Program to find the L.C.M. of two numbers

# define a function
def lcm(x, y):
   """ This function takes two integers and returns the LCM """

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3=  lcm(num1, num2)

print("The Least Common Multiple (LCM) of ", num1," and ", num2," is ", num3 )
