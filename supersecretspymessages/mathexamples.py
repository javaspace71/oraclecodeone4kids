import math

number1 = -100.8
number2 = -8.88
number3 = 2.12

print('First number is :', number1)
print('Floor value of first number is :', math.floor(number1))
print('Ceiling value of first number is :', math.ceil(number1))
print('Absolute value of first number is :', math.fabs(number1))
print('Rounding first number :', round(number1))
print('Truncating first number :', math.trunc(number1))
print('\n')

print('Second number is :', number2)
print('Floor value of second number is :', math.floor(number2))
print('Ceiling value of second number is :', math.ceil(number2))
print('Absolute value of second number is :', math.fabs(number2))
print('Rounding second number :', round(number2))
print('Truncating second number :', math.trunc(number2))
print('\n')

print('Third number is :', number3)
print('Floor value of third number is :', math.floor(number3))
print('Ceiling value of third number is :', math.ceil(number3))
print('Absolute value of third number is :', math.fabs(number3))
print('Rounding third number :', round(number3))
print('Truncating third number :', math.trunc(number3))
print('\n')

x = 64
y = 8
z = 2
print('sqrt of 64 is ', math.sqrt(x))
print('sqrt of 8 is ', math.sqrt(y))
print('sqrt of 2 is ', math.sqrt(z))

print('Value of apple pie = ', math.pi)

# Use math.pow method
n1 = math.pow(5, 3)

# Use operator
n2 = 2**5

# Print results
print("Using math.pow function, pow(5,3) is ", n1)
print("Using exponent operator, 2**5 is ", n2)

numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
anotherlist = [6, 12, 2]
sumlist = math.fsum(numlist)
anothersumlist = math.fsum(anotherlist)
print("Adding a list of numbers in numlist ", sumlist)
print("Adding a list of numbers in anotherlist ", anothersumlist)

facnum = math.factorial(5)
facnum2 = math.factorial(math.pi)
print("Factorial of 5, represented as 5! is ", facnum)
print("Factorial of 5, represented as 100! is ", facnum2)

