import random


class Cipher:
    def __init__(self):
        pass

    
    def caesar(self, str):
        from codecs import encode
        return encode(str, 'rot13')
    
words = ['ghosts', 'halloween', 'spirits', 'october', 'scary', 'spooky', 'spooktober']
print('The following is an encrypted text. Decrypt it to continue...')
myString = random.choice(words)
ciphered = Cipher().caesar(myString)

correct = False
while correct == False:
    print(ciphered)
    answer = input("Enter your decrypted message : ")
    if (Cipher().caesar(answer).lower().split() == ciphered.lower().split()): 
        print("Congratulations, you may continue.")
        correct = True
    else:
        print("Wrong Answer\n")