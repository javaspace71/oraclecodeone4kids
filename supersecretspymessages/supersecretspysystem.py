#!/bin/python3

alphabet = 'abcdefghijklmnopqrstuvwxyz'
#newMessage = ''

def encrypt(message, key):
  newMessage = ''
  print("encrypting ... ... ... ... ... done!")
  for character in message:
    if character in alphabet:
      position = alphabet.find(character)
      newPosition = (position + key) % 26
      newCharacter = alphabet[newPosition]
      newMessage += newCharacter
    else:
      newMessage += character
  print('Your new excrypted message is: ', newMessage)

  
def decrypt(message, key):
  newMessage = ''
  print("decrypting ... ... ... ... ... done!")
  for character in message:
    if character in alphabet:
      position = alphabet.find(character)
      newPosition = (position - key) % 26
      newCharacter = alphabet[newPosition]
      newMessage += newCharacter
    else:
      newMessage += character
  print('Your decrypted message is: ', newMessage)

while True:
  print("\n ******** SUPER SECRET SPY SYSTEM  *********\n")
  option = input("encrypt or decrypt (type e or d at the prompt)?")
  if(option == 'e'):
    print("super secret spy system is now ready to encrypt your message ....")
    message = input('Please enter a message: ')
    key = input('Enter a key (1-26): ')
    key = int(key)
    print("\n")
    encrypt(message, key)
    
  elif(option == 'd'):
    print("super secret spy system is now ready to decrypt the secret message ....")
    message = input('Please enter a message: ')
    key = input('Enter a key (1-26): ')
    key = int(key)
    print("\n")
    decrypt(message, key)

  elif(option == 'q'):
    exit()
    
  else:
    print("super secret spy system is watching you now ...")
    print("you can only encrypt or decrypt messages")


