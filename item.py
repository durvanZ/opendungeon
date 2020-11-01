class item :
    def __init__(self, id) :
        self.id = id
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
      
    def glow() :
        if (self.used != false) :
            print("you see a .....................") 
            show_options(self.options)

    def show_puzzle() :
        if puzzleId == 1 : 
            hangman.run(word)
        if puzzleId == 2 : 
            cypher.run(word)
        if puzzleId == 3 : 
            anagram.run(word)
        if puzzleId == 4 : 
            quiz.run(word)
    def open() :
        pass
    def read() :
        pass
    def inspect() :
        pass
    def eat() :
        pass
    def drink() :
        pass
    def smoke() :
        pass
    def ignore() :
        pass
    def show_options(self,listOfOptions):
            print("press: ")
            for option in listOfOptions :
                print("a. {0}".format(option))
    
    
