import s3e
import s3d

while True:
  print("\n ******** SUPER SECRET SPY SYSTEM  *********\n")
  option = input("encrypt or decrypt (type e or d at the prompt)?")
  
  if(option == 'e'):
    key = s3e.prompt_encrypt()
    s3e.secretalpha(key)
    s3e.encrypt(s3e.original_message, key)
    print('Your new excrypted message is: ', s3e.newMessage)
    s3e.newMessage = ""
    
  elif(option == 'd'):
    key = s3d.prompt_decrypt()
    s3d.decrypt(s3d.scrambled_message, key)
    print('Your decrypted message is: ', s3d.newMessage)
    s3d.newMessage = ""

  elif(option == 'q'):
    exit()
    
  else:
    print("super secret spy system is watching you now ...")
    print("you can only encrypt or decrypt messages")
