class hangman:
    def __init__(self) :
        pass

    def random_word(self, difficulty) :
        if difficulty == "easy" :print()
        if difficulty == "medium" : print()
        if difficulty == "hard" :print ()

    def run(self, word) :
        word = word
        l = len(word)
        if l <7 : max = 8
        if l >=7 : max = 13
        revealed = []
        displayed = []
        for i in word :
            displayed.append("_ ")
        for n in range(max) :
            for character in word : 
                for i in revealed :
                    if character==word[i] :
                        displayed[i] = character
                        break
            string = ""
            for x in displayed:
                string = string + x
            print(string)
            user_input = input("Enter your guess")
            counter = 0
            correct = False
            for character in word :
                if (user_input.lower() == character.lower()) :
                    revealed.append(counter)
                    correct = True
                counter = counter+1
            if (correct == True) :
                print("Correct. worse luck next time")
            else :
                print("WRONG!!!")
            n= n+1         