alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = ''
scrambled_message = ''
secretalphabet = ''
newMessage = ''

def prompt_decrypt():
  print("\n ******** SUPER SECRET SPY SYSTEM  *********\n")
  print("super secret spy system is watching you now ...")
  print("you can decrypt your message now")
  global scrambled_message
  scrambled_message = input('Please enter the scrambled message: ')
  key = input('Enter your key (1-26): ')
  key = int(key)
  print("\n")
  return key

def decrypt(message, key):
  global newMessage
  print("decrypting ... ... ... ... ... done!")
  for character in message:
    if character in alphabet:
      position = alphabet.find(character)
      newPosition = (position - key) % 26
      newCharacter = alphabet[newPosition]
      newMessage += newCharacter
    else:
      newMessage += character
