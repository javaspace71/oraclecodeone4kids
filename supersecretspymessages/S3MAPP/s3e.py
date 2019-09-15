alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 0
original_message = ''
secretalphabet = ''
newMessage = ''

def prompt_encrypt():
  print("\n :-) :-) :-) :-0 SUPER SECRET SPY SYSTEM  ??????????\n")
  print("super secret spy system is watching you now ...")
  print("you can encrypt your message now")
  global original_message
  original_message = input('Please enter a message: ')
  key = input('Enter a key (1-26): ')
  key = int(key)
  print("\n")
  print(alphabet)
  return key

def secretalpha(key):
  global secretalphabet
  for character in alphabet:
    position = alphabet.find(character)
    newPosition = (position + key) % 26
    secretcharacter = alphabet[newPosition]
    secretalphabet = secretalphabet + secretcharacter
  print(secretalphabet)
  print("\n")
  

def encrypt(message, key):
  global newMessage
  for character in message:
    if character in alphabet:
      position = alphabet.find(character)
      newPosition = (position + key) % 26
      newCharacter = alphabet[newPosition]
      newMessage = newMessage + newCharacter
    else:
      newMessage = newMessage + character

