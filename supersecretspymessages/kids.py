import os
while True:
    age = int(input("How old are you?: "))
    if age == 0:
        print("Thanks for playing!")
        exit()
    if age > 60:
        print("If you are more than", age, "years old then why are you in this class?")
    if age < 60 and age > 18:
        print("Good for you ... you must be a parent or college student")
    if age < 18 and age > 7:
        print("Hi cool kid! You are", age, " years old.  After this class, you can go play if you have done your HW!")
    if age < 8 and age > 0:
        print("you are too young for Python. Go program in Scratch")
    if age < 0:
        print("please behave")
