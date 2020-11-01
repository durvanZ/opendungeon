import random

class Cipher:
    def __init__(self):
        pass
    #Code for ROT-13 Caesar cipher
    def caesar(self, str):
        from codecs import encode
        return encode(str, 'rot13')
    #Run Cipher 
    def run(self):
        #List of words to by encrypted
        words = ['ghosts', 'halloween', 'spirits', 'october', 'scary', 'spooky', 'spooktober']
        print('The following is an encrypted text. Decrypt it to continue...')
        #Choose a random string from the words List
        myString = random.choice(words)
        #Given word goes through Caesar cipher
        ciphered = Cipher().caesar(myString)

        correct = False
        while correct == False:
            print(ciphered)
            answer = input("Enter your decrypted message : ")
            #If answer matches, congrats. Else, try again.
            if (Cipher().caesar(answer).lower().split() == ciphered.lower().split()): 
                print("Congratulations, you may continue.")
                correct = True
            else:
                print("Wrong Answer\n")