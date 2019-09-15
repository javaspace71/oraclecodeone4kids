'''  Using functions '''

def happyBirthday(person):
    #print("\n")
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday, dear " + person + ".")
    print("Happy Birthday to you!")
    print("\n")

def main():
    happyBirthday('John')
    happyBirthday('Jacob')
    happyBirthday('Jingleheimer Schmidt')

    #print("\n")
    userName = input("Enter the Birthday person's name: ")
    happyBirthday(userName)

    
main()
