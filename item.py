import hangman 
import Cipher
import quiz 

class item :
    def __init__(self,id,puzzleId) :

        self.id = id
        self.used = False
        if (self.id == 0) : self.options = []
        if self.id == 1 : self.options = []
        if self.id == 2 : self.options = []
        if self.id == 3 : self.options = []
        if self.id == 4 : self.options = []
        if self.id == 5 : self.options = []
        if self.id == 6 : self.options = []
        if self.id == 7 : self.options = []
        if self.id == 8 : self.options = []
        if self.id == 9 : self.options = []
        if self.id == 10 : self.options = []
        if self.id == 11 : self.options = []
        if self.id == 12 : self.options = []
        if self.id == 13 : self.options = []
      
    def glow(self) :
        if (self.used == False) :
            print("you see a .....................") 
            self.show_options(self.options)

    def show_puzzle() :
        if puzzleId == 1 : 
            hangman.run(hangman.random_word())
        if puzzleId == 2 : 
            Cipher.run()
        if puzzleId == 3 : 
            quiz.run(quiz.run.random_word())
    def open(self) :
        pass
    def read(self) :
        pass
    def inspect(self) :
        pass
    def eat(self) :
        pass
    def drink(self) :
        pass
    def smoke(self) :
        pass
    def ignore(self) :
        pass
    def show_options(self,listOfOptions):
            print("press: ")
            for option in listOfOptions :
                print("a. {0}".format(option))
    

